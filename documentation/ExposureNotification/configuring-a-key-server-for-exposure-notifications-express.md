# Configuring a Key Server for Exposure Notifications Express

**Framework**: Exposure Notification

Support exposure key upload and download for app-less exposure notifications.

#### Overview

Exposure Notifications Key Servers accept key uploads from users with positive diagnoses and enable key downloads to devices to support exposure detection. Exposure Notifications apps must use a specific file format for key archives, but a Public Health Authority (PHA) determines the method by which the server and client app exchange those key archives.

With Exposure Notifications Express, key servers must implement key upload and download as specified in this article, and must use Apple Business Registry (ABR) to configure the upload and download URLs and set other configurable options.

For more information on the key archive file formats, see [`Setting Up a Key Server`](setting-up-a-key-server.md).

##### Configure the Key Server

Exposure Notifications Express works by reading configuration values for a PHA from Apple Business Registry (ABR). It uses these configuration values to locate a PHA’s servers and to adjust its calculations and behavior based on the values entered by that PHA. In order to support key upload and download in Exposure Notifications Express, you must configure the following values:

- : The `tekPublishInterval` parameter identifies how often your server publishes new key archives, which are specified in increments of 10 minutes.
- : The `tekLocalDownloadIndexFile` parameter points to an index of key archives that are currently available from the key server.
- : The `tekLocalDownloadBasePath` value contains the base URL you use to retrieve key archives listed in the local download index. Exposure Notifications Express appends entries from the local download index file to this value to create a URL that points to the referenced file.
- : The `callbackIntervalInMin` parameter indicates how often iOS checks the key server for new archive files.
- : The `tekUploadURL` value points to the key server’s upload endpoint.

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

The `temporaryExposureKeys`array contains one JSON dictionary per key being uploaded. The per-exposure-key dictionary supports the keys listed below:

The key server responds to these requests by returning a JSON dictionary that describes the result in the response body. The response dictionary uses the keys listed below.

## See Also

- [Setting Up an Exposure Notifications Express Test Verification Server](setting-up-an-exposure-notifications-express-test-verification-server.md)
  Validate positive diagnoses for app-less exposure notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/configuring-a-key-server-for-exposure-notifications-express)*