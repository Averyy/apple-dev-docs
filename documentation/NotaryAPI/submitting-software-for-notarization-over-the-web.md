# Submitting software for notarization over the web

**Framework**: Notary API

Eliminate a dependency on macOS in your notarization workflow by interfacing directly with the notary service.

#### Overview

If you notarize macOS software that you distribute with Developer ID, and if you use a custom notarization workflow, you can use `notarytool` (included with Xcode) to interact with the notary service. However, if you want to avoid a macOS dependency for this part of the workflow, you can use the notary service’s REST API.

For an overview of the entire custom notarization workflow, see [`Customizing the notarization workflow`](https://developer.apple.com/documentation/Security/customizing-the-notarization-workflow). This article describes how to use the notary service API to replace the parts of that article that depend on `notarytool`, namely uploading your software and checking on the status of your request.

##### Create a Private Key

When you access the notary service, you authenticate the access by including a token that you sign with a private key. Use the same key to sign tokens for the notary service that you use for the App Store Connect API. For details on how to create a key, see [`Creating API Keys for App Store Connect API`](https://developer.apple.com/documentation/AppStoreConnectAPI/creating-api-keys-for-app-store-connect-api).

Keep the key secure and private. You only need to create a key once, but if you lose the key, or if the key becomes compromised, revoke it immediately and create a new one. For more information, see [`Revoking API Keys`](https://developer.apple.com/documentation/AppStoreConnectAPI/revoking-api-keys).

##### Include a Signed Token with Each Api Access

The notary service requires a JSON Web Token (JWT) to authorize each API request. JWT is an open standard ([`RFC 7519`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519)) that defines a way to securely transmit information by using a private key to cryptographically sign a message in JSON format. You use the key to create a JWT for each request. For more information, see [`Generating Tokens for API Requests`](https://developer.apple.com/documentation/AppStoreConnectAPI/generating-tokens-for-api-requests).

After creating the signed token, include it in the header for all of your notary service API calls. For example, to use the [`Get Previous Submissions`](get-previous-submissions.md) endpoint to get a list of up to 100 of your team’s previous notarization submissions, replace `<token>` in the following call to the `curl` command with your signed token:

```shell
% curl -v -H "Authorization: Bearer <token>" "https://appstoreconnect.apple.com/notary/v2/submissions"
```

Create a token that expires a short time after you create it — for example, 20 minutes. You can reuse a token until it expires.

##### Start a Submission

To submit a new version of your software for notarization, start by calling the [`Submit Software`](submit-software.md) endpoint. This call doesn’t upload your software; it tells the notary service to prepare for a new upload, and returns information that you use to perform the upload. Prepare the body of the request with a name and a hash of the software that you want to notarize, as well as optional information about how to notify you when notarization completes. For example, you can create a `body` variable in Python for a file named `OvernightTextEditor_11.6.8.zip`:

```bash
#!/usr/bin/env python3

import hashlib

with open("OvernightTextEditor_11.6.8.zip", "rb") as file:
    hash = hashlib.sha256()
    hash.update(file.read())
    sha256 = hash.hexdigest()

body = {
    "submissionName": "OvernightTextEditor_11.6.8.zip",
    "sha256": sha256,
    "notifications": [{"channel": "webhook", "target": "https://example.com" }]
}
```

The `body` consists of three keys, one of which is optional:

Use the `body`, plus the token described in the previous section, to call the endpoint and get a response. The following code continues from the previous Python example:

```python
import requests

token = generate_token() # Defined elsewhere.
resp = requests.post("https://appstoreconnect.apple.com/notary/v2/submissions", json=body, headers={"Authorization": "Bearer " + token})
resp.raise_for_status()
output = resp.json()
```

The service responds with an identifier that you use to track your submission, and temporary security credentials that you use to upload your software to an Amazon S3 endpoint. An example response looks like this:

```javascript
{
  "data": {
    "attributes": {
      "awsAccessKeyId": "ASIAIOSFODNN7EXAMPLE",
      "awsSecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      "awsSessionToken": "AQoDYXdzEJr...",
      "bucket": "EXAMPLE-BUCKET",
      "object": "EXAMPLE-KEY-NAME"
    },
    "id": "2efe2717-52ef-43a5-96dc-0797e4ca1041",
    "type": "submissionsPostResponse"
  },
  "meta": {
  }
} 
```

Store the identifier (`id`) so you can use it to ask the notary service about the status of the submission, and to retrieve information about the outcome of the notarization. If you lose the identifier, you can use the [`Get Previous Submissions`](get-previous-submissions.md) endpoint to get a list of the 100 most recent submissions associated with your team.

##### Upload Your Software

Use the `attributes` object that appears in the response from the [`Submit Software`](submit-software.md) call to upload your software to Amazon S3. A good way to do this is with the `boto3` library, provided by Amazon:

```python
import boto3

aws_info = output["data"]["attributes"]
bucket = aws_info["bucket"]
key = aws_info["object"]
sub_id = output["data"]["id"]

s3 = boto3.client(
         "s3",
         aws_access_key_id=aws_info["awsAccessKeyId"],
         aws_secret_access_key=aws_info["awsSecretAccessKey"],
         aws_session_token=aws_info["awsSessionToken"],
         config=Config(s3={"use_accelerate_endpoint": True})
)

resp = s3.upload_file("OvernightTextEditor_11.6.8.zip", bucket, key)
```

The temporary S3 credentials contained in the attributes object expire 12 hours after you get them from the notary service. If you don’t use the credentials before they expire, you’ll have to restart the upload process. For more information about using this library and accessing Amazon S3, see the documentation on [`https://aws.amazon.com`](https://developer.apple.comhttps://aws.amazon.com).

##### Check the Status of Your Submission

Notarization typically takes just a few minutes after you complete the upload. To verify the status of your submission, you can call the [`Get Submission Status`](get-submission-status.md) endpoint by using the following `curl` command along with the identifier that the service returned when you started the submission:

```shell
% curl -v -H "Authorization: Bearer <token>" "https://appstoreconnect.apple.com/notary/v2/submissions/2efe2717-52ef-43a5-96dc-0797e4ca1041"
```

After notarization completes, use the [`Get Submission Log`](get-submission-log.md) endpoint to get a log file that contains any notarization errors or warnings:

```shell
% curl -v -H "Authorization: Bearer <token>" "https://appstoreconnect.apple.com/notary/v2/submissions/2EFE2717-52EF-43A5-96DC-0797E4CA1041/logs"
```

This call returns a URL that you can use to download a log file in JSON format. The log file provides details about the notarization outcome for this particular submission. The log file URL is valid for only a few hours, but you can ask for a new URL later if you need the log again. Always check the log file, even if notarization succeeds, because it might contain warnings that you can fix prior to your next submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submitting-software-for-notarization-over-the-web)*