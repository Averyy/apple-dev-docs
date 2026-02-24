# Configuring a Key Server for Exposure Notifications Express

**Framework**: Exposure Notification

Support exposure key upload and download for app-less exposure notifications.

#### Overview

Exposure Notifications Key Servers accept key uploads from users with positive diagnoses and enable key downloads to devices to support exposure detection. Exposure Notifications apps must use a specific file format for key archives, but a Public Health Authority (PHA) determines the method by which the server and client app exchange those key archives.

With Exposure Notifications Express, key servers must implement key upload and download as specified in this article, and must use Apple Business Registry (ABR) to configure the upload and download URLs and set other configurable options.

For more information on the key archive file formats, see [`Setting Up a Key Server`](setting-up-a-key-server.md).

##### Configure the Key Server

Exposure Notifications Express works by reading configuration values for a PHA from Apple Business Registry (ABR). It uses these configuration values to locate a PHA’s servers and to adjust its calculations and behavior based on the values entered by that PHA. In order to support key upload and download in Exposure Notifications Express, you must configure the following values:

- **Publish Interval**: The `tekPublishInterval` parameter identifies how often your server publishes new key archives, which are specified in increments of 10 minutes.
- **Local Download Index File**: The `tekLocalDownloadIndexFile` parameter points to an index of key archives that are currently available from the key server.
- **Local Download Base Path**: The `tekLocalDownloadBasePath` value contains the base URL you use to retrieve key archives listed in the local download index. Exposure Notifications Express appends entries from the local download index file to this value to create a URL that points to the referenced file.
- **Callback Interval in Minutes**: The `callbackIntervalInMin` parameter indicates how often iOS checks the key server for new archive files.
- **Key Upload URL**: The `tekUploadURL` value points to the key server’s upload endpoint.

For a complete list of the configuration options available with Exposure Notifications Express, see [`Configuring Exposure Notifications`](configuring-exposure-notifications.md).

##### Publish an Index File

To support Exposure Notification Express, key servers must publish an index file at the Local Download Index File URL (`tekLocalDownloadIndexFile)` registered in ABR. Index files are UTF-8 text files that contain one line per key archive that is currently available from the key server. The index lists archive files in chronological order, with the oldest key archive on the first line of the file. As the key server adds new files to the index, it also removes any entry pointing to archives more than 14–days old.

##### Publish Key Batches As Zip Archives

Key servers periodically publish new key archives that contain any new diagnosis keys uploaded to the server since the last time it published an archive. Health Authorities register a configuration value (`callbackIntervalInMin`) in ABR to control the frequency of the updates. When the server publishes a new key file, it adds the URL of that new archive (excluding the base URL) as the first entry in the local download index file.

Exposure Notifications Express uses the same key archive file format as Exposure Notification client apps. Each archive contains one `.dat` and one `.sig` file, as specified in [`Setting Up a Key Server`](setting-up-a-key-server.md).

When a user enables COVID-19 exposure notifications, Exposure Notifications Express queries the key server’s local download index file to retrieve the index. Exposure Notifications Express then uses that index to retrieve all keys from the key server for the last 14 days. You don’t need to use a specific naming convention to publish key archives, but incorporating region, start time, and end time into the filename simplifies debugging and clarifies logging.

##### Accept Key Uploads

To support Exposure Notifications Express key uploads, a key server must implement the Key Upload URL (`tekUploadURL`) configured in ABR. iOS uploads key batches to that URL by sending a JSON dictionary as the body of an HTTP POST request with all the data the key server needs to authenticate the keys and the diagnosis.

The request dictionary uses the keys listed below:

- **`temporaryExposureKeys`**: An array of temporary exposure keys (*see below*).**Required**.
- **`healthAuthorityID`**: An identifier string for the mobile application that submits the keys or a unique string that identifies the PHA when using Exposure Notifications Express.**Required**.
- **`verificationPayload`**: The verification certificate from the test verification server.
- **`hmacKey`**: A device-generated string containing a secret code the key server uses to recalculate the HMAC value.
- **`symptomOnsetInterval`**: An integer representing the interval number that aligns with the symptom onset date.
- **`revisionToken`**: An opaque string the key server returned in a previous call to this endpoint. If included, the key server uses this token to apply the data in the uploaded keys as an update to existing keys. When Exposure Notifications Express uploads only new keys, this field will contain an empty string.**Required**.
- **`padding`**: Random data iOS may populate to obscure the request size. Don’t process data in this field.

The `temporaryExposureKeys`array contains one JSON dictionary per key being uploaded. The per-exposure-key dictionary supports the keys listed below:

- **`key`**: The 16-byte exposure key as a Base64-encoded string. If a key is not exactly 16 bytes in length, the key server rejects the entire request, not just the key that is too long.**Required**.
- **`rollingStartNumber`**: An integer representing the interval number when the key’s`EKRollingPeriod`started.**Required**.
- **`rollingPeriod`**: An integer representing the duration for which the key is valid, expressed as a number of ten–minute intervals.**Required**.
- **`transmissionRisk`**: Risk of transmission associated with the person from which this key came. This field is deprecated and may be removed in a future release.

The key server responds to these requests by returning a JSON dictionary that describes the result in the response body. The response dictionary uses the keys listed below.

- **`revisionToken`**: A revision token string you use during future key uploads if the diagnosis associated with the uploaded keys changes.
- **`insertedExposures`**: An integer representing the number of exposure keys the key server added to its database.
- **`error`**: If the server encounters an error while processing the request, this string contains a description of the problem.
- **`errorCode`**: If the server encounters an error while processing the request, this string contains a code that describes the error.
- **`padding`**: String the server may populate with random data to obscure the response size. Don’t process data in this field.

## See Also

- [Setting Up an Exposure Notifications Express Test Verification Server](setting-up-an-exposure-notifications-express-test-verification-server.md)
  Validate positive diagnoses for app-less exposure notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/configuring-a-key-server-for-exposure-notifications-express)*