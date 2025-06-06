# Setting Up an Exposure Notifications Express Test Verification Server

**Framework**: Exposure Notification

Validate positive diagnoses for app-less exposure notifications.

#### Overview

Exposure Notifications Express requires a Public Health Authority (PHA) to have a test verification server that verifies positive diagnoses received from a test center or other healthcare provider. A test verification server includes a mechanism to request a verification code for users with a positive COVID-19 test result. The test verification server also has APIs that allow Exposure Notifications Express to authenticate the user’s positive diagnosis before uploading exposure keys to the PHA’s key server

Google has created a reference implementation of a [`test verification server`](https://developer.apple.comhttps://github.com/google/exposure-notifications-verification-server) that you can use as a starting point or as a reference while implementing your own test verification server.

##### Configure the Test Verification Server

Exposure Notifications Express works by reading configuration values for a PHA from Apple Business Registry (ABR). It uses these configuration values to locate a PHA’s servers and to adjust its calculations and behavior based on the values entered by that PHA. To set up a test verification server to work with Exposure Notifications Express, a PHA specifies the following values:

- : The `testVerificationIntroMessage` is a string that iOS presents to the user to explain the purpose of test verification and key upload.
- : Exposure Notifications Express uses the `testVerificationURL` to exchange verification codes for long-term authentication tokens.
- : Exposure Notifications Express uses the `testVerificationCertificateURL` to upload an HMAC and long-term authentication token and receive back a certificate and key metadata.
- : iOS needs the value in `testVerificationAPIKey` to communicate with your test verification server.
- : Exposure Notifications Express presents the `verificationCodeLearnMoreURL` to the user when they have received a positive diagnosis. The link contains information on how to use the verification code and provides way to request help if the user experiences problems.

To see all of the configuration options available with Exposure Notifications Express, see [`Configuring Exposure Notifications`](configuring-exposure-notifications.md).

##### Generate Verification Codes on Request

PHAs use the test verification server to generate verification codes for positive test results. The verification code may be an 8-digit number that can be read over the phone or a deep link that can be texted or emailed to the user. A test verification server can use any one-time password algorithm to generate a verification code as long as the resulting code uniquely identifies one test result.

> **Note**:  For information on generating deep links that are compatible with Exposure Notifications Express, see [`Exposure Notifications Server Resource Identifier Scheme Documentation`](https://developer.apple.comhttps://github.com/google/exposure-notifications-verification-server/blob/main/docs/ens-spec.md).

 For information on generating deep links that are compatible with Exposure Notifications Express, see [`Exposure Notifications Server Resource Identifier Scheme Documentation`](https://developer.apple.comhttps://github.com/google/exposure-notifications-verification-server/blob/main/docs/ens-spec.md).

##### Exchange Verification Codes for Tokens

Test verification servers must provide an endpoint to allow an iPhone to exchange a verification code for a long-term authentication token. PHAs register the URL for this endpoint with ABR as the Test Verification URL (`testVerificationURL`). This endpoint expects a JSON dictionary as the body of an HTTP POST request.

This endpoint supports one key in the request dictionary:

Requests must also include a custom HTTP header field called `X-API-Key`, with its value set to the test verification server’s secret API key. Test verification servers reject requests without this header or if the value in the header doesn’t match the API key registered with ABR.

The test verification server responds to these requests by returning a JSON dictionary in the body of the response. Here are the keys that the response dictionary uses:

##### Respond to Verification Certificate Requests

Before uploading keys to the key server, Exposure Notifications Express contacts the verification server at the Test Verification Certificate URL (`testVerificationCertificateURL`) registered with ABR to get a certificate and metadata for the key batch.

The test verification server expects requests to this URL to contain a JSON dictionary in the body of an HTTP POST request. Here are the keys that dictionary supports:

Requests to this URL must also include a custom HTTP header field called `X-API-Key`, with its value set to the test verification server’s API key. Test verification servers reject requests without this header, or with the wrong value in the header.

The test validation server responds to requests by returning JSON in the body of the response. Here are the keys for that response dictionary:

## See Also

- [Configuring a Key Server for Exposure Notifications Express](configuring-a-key-server-for-exposure-notifications-express.md)
  Support exposure key upload and download for app-less exposure notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/setting-up-an-exposure-notifications-express-test-verification-server)*