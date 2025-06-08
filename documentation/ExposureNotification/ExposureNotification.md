# Exposure Notification

**Framework**: Exposure Notification  
**Kind**: module

Implement a COVID-19 exposure notification system that protects user privacy.

**Availability**:
- iOS 13.5+
- iPadOS 13.5+
- Mac Catalyst 13.5+

## Mentions

- [Setting Up a Key Server](setting-up-a-key-server.md)

#### Overview

Use the Exposure Notification framework to inform people of potential exposure to COVID-19, the disease caused by the SARS-CoV-2 virus. You can build a notification system that employs random, rotating keys and identifiers to convey positive diagnoses in addition to data such as associated symptoms, proximity, and duration.

##### Establish User Roles

The ExposureNotification framework defines two user roles:

> ❗ **Important**:  Before you can develop an app that uses ExposureNotification, you need the [`com.apple.developer.exposure-notification`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.exposure-notification) entitlement. For more information on this entitlement, see [`Exposure Notification APIs Addendum`](https://developer.apple.comhttps://developer.apple.com/contact/request/download/Exposure_Notification_Addendum.pdf). To get permission to use this entitlement, see [`Exposure Notification Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/exposure-notification-entitlement).

##### Identify Your Apps Region

All EN apps must specify the region for which they work by adding a key called [`ENDeveloperRegion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENDeveloperRegion) to the app’s `Info.plist` file. The value for `ENDeveloperRegion` is set to a string that represents the app’s region. This value can be an ISO 3166-1 country code (for example, “CA” for Canada), or the ISO 3166-1/3166-2 country code plus subdivision code (“US-CA” for California).

Explicitly set the associated domain link to your region code. Avoid using wildcards because they can impact system operations. See [`Associated Domains Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains) for more information.

##### Specify Exposure Notification Api Version

iOS 13.7 introduces a new method of calculating the user’s Exposure Risk Value, described in [`ENExposureConfiguration`](enexposureconfiguration.md). Apps can implement this new method, or continue to use the calculation method introduced in earlier versions of iOS. To choose your app’s approach, add an entry to your app’s `Info.plist` file with a key of [`ENAPIVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion). To use the new approach, specify a value of `2`. To use the original approach, specify a value of `1`.

##### Support Exposure Notification Express

Starting with iOS 13.7, Health Authorities can inform users of potential exposure to COVID-19 without a dedicated Exposure Notification app. This feature is called Exposure Notification Express and must be enabled by a Health Authority. For more information, see [`Supporting Exposure Notifications Express`](supporting-exposure-notifications-express.md).

## Topics

### Essentials
- [Supporting Exposure Notifications Express](supporting-exposure-notifications-express.md)
  Configure servers to notify users of potential exposures to COVID-19 without an app.
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
### Exposures
- [Configuring Exposure Notifications](configuring-exposure-notifications.md)
  Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- [class ENExposureConfiguration](enexposureconfiguration.md)
  The object that contains parameters for configuring exposure notification risk scoring behavior.
- [class ENExposureWindow](enexposurewindow.md)
  A set of scan events from observed beacons within a time span.
- [class ENScanInstance](enscaninstance.md)
  The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](exposure-parameter-limits.md)
  The limits for the parameters you use in exposure risk calculations.
### Summaries
- [class ENExposureDetectionSummary](enexposuredetectionsummary.md)
  A summary of exposures.
- [class ENExposureDaySummary](enexposuredaysummary.md)
  The summary of exposure information for a single day.
- [class ENExposureSummaryItem](enexposuresummaryitem.md)
  The summary of exposures for a specific time period or report type.
### Status
- [enum ENAuthorizationStatus](enauthorizationstatus.md)
  A set of cases that indicates the authorization status for the app.
- [enum ENStatus](enstatus.md)
  A set of cases that represents the overall status of exposure notification on the system.
### Errors
- [struct ENError](enerror.md)
  Errors that the exposure notification framework issues.
- [ENError.Code](enerror/code.md)
  Error codes that the exposure notification framework issues.
- [let ENErrorDomain: String](enerrordomain.md)
  The domain for an error.
- [typealias ENErrorHandler](enerrorhandler.md)
  The handler for error conditions.
### Variables
- [var ENRiskWeightDefaultV2: Int](enriskweightdefaultv2.md)
  This weight is not used.
- [var ENRiskWeightMaxV2: Int](enriskweightmaxv2.md)
  This weight is not used.
- [var EN_FEATURE_GENERAL: Int32](en_feature_general.md)
### Type Aliases
- [typealias ENDetectExposuresHandler](endetectexposureshandler.md)
  The definition of a handler that returns exposure summaries.
- [typealias ENErrorOutType](enerrorouttype.md)
  Type for returning NSError’s from functions. Avoids long and repetitious method signatures.
- [typealias ENGetDiagnosisKeysHandler](engetdiagnosiskeyshandler.md)
  The definition of a handler that returns diagnosis keys.
- [typealias ENGetExposureInfoHandler](engetexposureinfohandler.md)
  The definition of a handler that receives exposure info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExposureNotification)*