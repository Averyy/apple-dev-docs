# Supporting Exposure Notifications Express

**Framework**: Exposurenotification

Configure servers to notify users of potential exposures to COVID-19 without an app.

#### Overview

iOS 13.7 and later can inform people of potential exposure to COVID-19 without a dedicated Exposure Notifications app. This app-less functionality is called Exposure Notifications Express and is only available when a Public Health Authority (PHA) supports it.

iOS continues to support dedicated Exposure Notifications apps, and a PHA can offer Exposure Notifications apps and the app-less Exposure Notifications Express at the same time. When a user enables Exposure Logging, iOS uses the PHA’s app if one is installed, and falls back to the app-less experience if no app is installed and the PHA supports Exposure Notifications Express.

##### Deploy Exposure Notifications Express Servers

To support Exposure Notifications Express, a PHA must deploy two different types of servers:

- : Validates positive diagnoses during key upload. For more information, see [`Setting Up an Exposure Notifications Express Test Verification Server`](setting-up-an-exposure-notifications-express-test-verification-server.md).
-  Handles key uploads and downloads. The same key server handles key upload and download for Exposure Notifications apps and Exposure Notifications Express. For more information, see [`Configuring a Key Server for Exposure Notifications Express`](configuring-a-key-server-for-exposure-notifications-express.md). For information on setting up a key server, see [`Setting Up a Key Server`](setting-up-a-key-server.md).

> **Note**:  Prior to the introduction of Exposure Notifications Express in iOS 13.7, the Exposure Notifications Key Server was referred to as the “Exposure Notifications Server” or the “EN Server”.

##### Verify Diagnoses and Send Notifications

Exposure Notifications Express works by communicating with the test verification server and the key server at specific times in a defined process, as depicted in the figure below.

![Diagram of the Exposure Notifications Express process with the actors in the steps listed in chronological order from left to right, including a PHA, a user, a test verification server, the user’s iPhone, and a key server. Underneath the icons depicting the actors is a chart of the steps the actors take with arrows indicating what direction information moves through the Exposure Notifications Express timeline.](https://docs-assets.developer.apple.com/published/8dbab23b2c12fe6941a934ff7f531fd3/media-3680724%402x.png)

Here are the steps involved with verifying and submitting a positive diagnosis with Exposure Notifications Express.

1. First, a user with Exposure Notifications enabled on their iPhone running iOS 13.7 or later gets tested for COVID-19.
2. The test center or other health care provider determines that the user has a positive test result and reports it to the PHA.
3. The PHA generates a verification code using the test verification server.
4. The PHA sends the verification code to the user. The code may be emailed, read over the phone, or provided as a clickable deep link in a text message.
5. The user enters the verification code or clicks the provided link to inform their iPhone of the positive diagnosis.
6. The user’s iPhone contacts the test verification server to validate the verification code. If the code is valid, it receives back a long-term authentication token from the test verification server and stores it.
7. If necessary, the user’s iPhone prompts the user for additional information.
8. The user’s iPhone creates a hashed message authentication code (HMAC) calculated from the user’s exposure key data and sends it to the test verification server along with the user’s authentication token, receiving in return a certificate and additional per-key metadata. For more information on the HMAC calculation, see [`Public Health Authority Diagnosis Verification Protocol`](https://developer.apple.comhttps://github.com/google/exposure-notifications-server/blob/main/docs/design/verification_protocol.md).
9. The user’s iPhone validates the returned certificate and metadata and stores them.
10. iPhone prompts the user for permission to submit their keys to the key server.
11. If the user grants permission, their iPhone uploads their temporary exposure keys to the key server along with the authentication token, certificate, and metadata received from the test verification server.
12. If the test verification server validates the uploaded keys, it adds them to its database and returns a revision token that can be used to upload a diagnosis change for the uploaded keys.

The validated and uploaded keys are available for download by other devices to be used for on-device exposure detection. To look at a sample implementation of a key server that supports both Exposure Notifications Express as well as Exposure Notifications client apps, see [`Exposure Notifications Reference Key Server`](https://developer.apple.comhttps://github.com/google/exposure-notifications-server). To look at a sample implementation of a test verification server, see [`Exposure Notifications Verification System Reference Server`](https://developer.apple.comhttps://github.com/google/exposure-notifications-verification-server).

## Topics

### Server Configuration
- [Setting Up an Exposure Notifications Express Test Verification Server](setting-up-an-exposure-notifications-express-test-verification-server.md)
  Validate positive diagnoses for app-less exposure notifications.
- [Configuring a Key Server for Exposure Notifications Express](configuring-a-key-server-for-exposure-notifications-express.md)
  Support exposure key upload and download for app-less exposure notifications.

## See Also

- [Building an App to Notify Users of COVID-19 Exposure](building-an-app-to-notify-users-of-covid-19-exposure.md)
  Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](setting-up-a-key-server.md)
  Ensure that your server meets the requirements for supporting Exposure Notifications.
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

*[View on Apple Developer](https://developer.apple.com/documentation/ExposureNotification/supporting-exposure-notifications-express)*