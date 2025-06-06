# Setting Up a Key Server

**Framework**: Exposure Notification

Ensure that your server meets the requirements for supporting Exposure Notifications.

#### Overview

Apps that use the [`Exposure Notification`](ExposureNotification.md) framework rely on a key server to identify potential exposure to individuals diagnosed with COVID-19, the disease caused by the SARS-CoV-2 virus. The key server is responsible for collecting and distributing exposure keys to allow on-device exposure detection. This article describes how to provide the data that allows exposure notification to work, and details the data format the [`Exposure Notification`](ExposureNotification.md) framework requires.

A key server, at a minimum, must allow exposure notification clients to:

- Retrieve diagnosis keys so they can check for potential exposures
- Submit temporary exposure keys

If providing a client app, a Health Authority can choose how to implement these capabilities as long as the data that passes to and from the exposure notification client conforms to the data formats this article describes. To support Exposure Notifications Express, which allows exposure notifications without an app in iOS 13.7 and above, a key server’s functionality must conform to specific requirements. For more information on how to support Exposure Notifications Express with your key server, see [`Configuring a Key Server for Exposure Notifications Express`](configuring-a-key-server-for-exposure-notifications-express.md).

Google has created an [`implementation of a key server `](https://developer.apple.comhttps://github.com/google/exposure-notifications-server/)that you can use as a reference, or as a starting point for creating your own key server.

> **Note**:  Diagnosis keys are temporary exposure keys for individuals who have had a positive diagnosis of COVID-19.

 Diagnosis keys are temporary exposure keys for individuals who have had a positive diagnosis of COVID-19.

Before you begin setting up your key server, [`request an Exposure Notification Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/exposure-notification-entitlement). Once your request is accepted, you’ll be asked to provide information that clients will use to authenticate the data they receive from your server, such as its public key.

##### Reject Invalid Temporary Exposure Keys

A key server must reject invalid key files uploaded from a client app. Uploaded key data is considered invalid if:

- The period of time covered by the data file exceeds 14 days
- `TEKRollingPeriod`, if included, must be a positive value that is no greater than 144

If `TEKRollingPeriod` is not included, use a default value of 144. You may optionally want to validate the clock time the device submits.

For detailed information on implementing key validity checks, see [`Exposure Notification Cryptography Specification`](https://developer.apple.comhttps://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-CryptographySpecificationv1.2.pdf).

##### Take Precautions with Temporary Exposure Keys

To help ensure that the data sent to client devices canʼt be used to reveal a userʼs identity, your key server:

- Must store temporary exposure keys in randomized order, not in the order in which theyʼre received, and not grouped by user
- Must not distribute temporary exposure key data until at least 2 hours after the end of the keyʼs expiration window
- Must periodically delete any stored temporary exposure keys to ensure that none are over 30 days old

##### Sign Downloads with the Latest Registered Certificate

A key server must always sign files with the private key that corresponds to the latest public key provided to Apple using SHA-256 with ECDSA. Exposure notification clients reject keys retrieved from a server when they can’t verify them against the current public key.

##### Package Temporary Exposure Key Data in a Zip Archive

A key server must deliver diagnosis key data to clients as a zip archive that contains two files, both stored at the root level, and both with the same base name, but different extensions. The file that contains the temporary exposure key data must have the extension `.bin` and the file that contains the signature and signature-verification metadata must have the extension `.sig`.

A key server can send multiple zip archives to the same client, but each archive sent at the same time must use different base names for the contained files. For compatibility, send a maximum of 15 key files to a single client in a 24-hour period, because clients running on iOS 13.5 and earlier are limited to 15 key files in this time frame.

For best results, zip archives should be no larger than 16 MB and contain no more than 750,000 keys.

> **Note**:  While both the key and signature file specifications support multi-file batches, not all exposure notification clients accept them. To ensure that all clients can accept your key server’s diagnosis keys, always set `batch_num` and `batch_size` to a value of 1.

 While both the key and signature file specifications support multi-file batches, not all exposure notification clients accept them. To ensure that all clients can accept your key server’s diagnosis keys, always set `batch_num` and `batch_size` to a value of 1.

The `.bin` file in the zip archive is a binary file that begins with a 16-byte header that contains `​EK Export v1`​  in UTF-8 encoding, right-padded with whitespace characters. This header represents the current version of the exposure-key binary format. The header is followed by a serialized ​protocol buffer​ message named `TemporaryExposureKeyExport`,​ which uses the following protocol buffer definition:

```swift
syntax = "proto2";
message TemporaryExposureKeyExport {
    // Time window of keys in the file, based on arrival
    // at the server, in UTC seconds.
    optional fixed64 start_timestamp = 1;
    optional fixed64 end_timestamp = 2;

    // The region from which these keys came
    optional string region = 3;

    // Reserved for future use. Both batch_num and batch_size
    // must be set to a value of 1.
    optional int32 batch_num = 4;
    optional int32 batch_size = 5;

    // Information about associated signatures
    repeated SignatureInfo signature_infos = 6;
    
    // Exposure keys that are new. 
    repeated TemporaryExposureKey keys = 7;
    
    // Keys that have changed status from previous key archives,
    // including keys that are being revoked.
    repeated TemporaryExposureKey revised_keys = 8;
}
message SignatureInfo {
    // The first two fields have been deprecated.
    reserved 1, 2;
    reserved "app_bundle_id", "android_package";
    
    // Key version in case the key server signing key is rotated. (e.g. "v1")
    // A PHA can only have one active public key at a time, so they must rotate
    // keys on all devices and servers at the same time to avoid problems.
    optional string verification_key_version = 3;
    
    // Implementation-specific string that can be used in key verification.
    // Valid character in this string are all alphanumeric characters, 
    // underscores, and periods.
    optional string verification_key_id = 4;

    // All keys must be signed using the SHA-256 with ECDSA algorithm.
    // This field must contain the string "1.2.840.10045.4.3.2". 
    optional string signature_algorithm = 5;
}
message TemporaryExposureKey {
    // Temporary exposure key for an infected user.
    optional bytes key_data = 1;
    
    // Varying risk associated with a key depending on diagnosis method. 
    // Deprecated and no longer used.
    optional int32 transmission_risk_level = 2 [deprecated = true];
    
    // The interval number since epoch for which a key starts
    optional int32 rolling_start_interval_number = 3;
    
    // How long this key is valid, specified in increments of 10 minutes
    optional int32 rolling_period = 4
    [default = 144]; // defaults to 24 hours
    
    // Data type that represents why this key was published.
    enum ReportType {
      UNKNOWN = 0;  // Never returned by the client API.
      CONFIRMED_TEST = 1;
      CONFIRMED_CLINICAL_DIAGNOSIS = 2;
      SELF_REPORT = 3;
      RECURSIVE = 4;  // Reserved for future use.
      REVOKED = 5;  // Used to revoke a key, never returned by client API.
    }

    // Type of diagnosis associated with a key.
    optional ReportType report_type = 5;

    // Number of days elapsed between symptom onset and the TEK being used.
    // E.g. 2 means TEK is from 2 days after onset of symptoms.
    // Valid values range is from -14 to 14.
    optional sint32 days_since_onset_of_symptoms = 6;
}
```

The `.sig` file in the archive contains the signature and information the client needs to validate the download. The key server generates the signature file by serializing a single `TEKSignatureList` protocol buffer message, which uses the following protocol buffer definition:

```swift
syntax = "proto2";
 
message TEKSignatureList {
    // Information about associated signatures
    repeated TEKSignature signatures = 1;
}

message TEKSignature {
    // Information to uniquely identify the public key associated 
    // with the key server's signing key.
    optional SignatureInfo signature_info = 1;

    // Reserved for future use. Both batch_num and batch_size
    // must be set to a value of 1.
    optional int32 batch_num = 2; 
    optional int32 batch_size = 3;

    // Signature in X9.62 format (ASN.1 SEQUENCE of two INTEGER fields).
    optional bytes signature = 4;    
}

```

To calculate the `signature` data inside a `TEKSignature` message, start by generating a digest of the data file in the archive using the SHA-256 hash algorithm. Then, sign the digest value using the ECDSA with P-256 algorithm. The private key you use for signing must be the one that corresponds to the public key registered with Appleʼs key server.

## See Also

- [Supporting Exposure Notifications Express](supporting-exposure-notifications-express.md)
  Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](building-an-app-to-notify-users-of-covid-19-exposure.md)
  Inform people when they may have been exposed to COVID-19.
- [class ENManager](enmanager.md)
  A class that manages exposure notifications.
- [ENDeveloperRegion](../BundleResources/Information-Property-List/ENDeveloperRegion.md)
  A string that specifies the region that the app supports.
- [ENAPIVersion](../BundleResources/Information-Property-List/ENAPIVersion.md)
  A number that specifies the version of the API to use.
- [Changing Configuration Values Using the Server‑to‑Server API](changing-configuration-values-using-the-server-to-server-api.md)
  Update Exposure Notifications configuration values from a Public Health Authority’s server.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](testing-exposure-notifications-apps-in-ios-13-7-and-later.md)
  Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.
- [Supporting Exposure Notifications in iOS 12.5](supporting-exposure-notifications-in-ios-12-5.md)
  Prepare your Exposure Notifications app to run on a previous version of iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/setting-up-a-key-server)*