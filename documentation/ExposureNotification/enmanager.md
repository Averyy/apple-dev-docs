# ENManager

**Framework**: Exposure Notification  
**Kind**: class

A class that manages exposure notifications.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENManager
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.5 and later.

 This class is available in iOS 12.5, and in iOS 13.5 and later.

Before using an instance of this class, call [`activate(completionHandler:)`](enmanager/activate(completionhandler:).md). If the completion handler completes successfully, you can work with the remaining properties and methods on the class. Activating this object doesn’t enable exposure notification; it only allows this object to be used. Once activated, exposure notification can be enabled with [`setExposureNotificationEnabled(_:completionHandler:)`](enmanager/setexposurenotificationenabled(_:completionhandler:).md), if needed.

If the app no longer needs an instance of this class, you must call [`invalidate()`](enmanager/invalidate().md), which stops any outstanding operations and invokes the invalidation handler.

> **Note**:  Invalidation is asynchronous so it’s possible for handlers to be invoked after calling [`invalidate()`](enmanager/invalidate().md).

 Invalidation is asynchronous so it’s possible for handlers to be invoked after calling [`invalidate()`](enmanager/invalidate().md).

The framework invokes the invalidation handler once invalidation finishes, and performs the invocation exactly once, even if [`invalidate()`](enmanager/invalidate().md) is called multiple times. It does not call any additional handlers.

After calling [`invalidate()`](enmanager/invalidate().md), your app can’t reuse the object. A new object must be created for subsequent use. The framework clears strong references once invalidation completes to break potential retain cycles. You don’t need to use weak references within your handlers to avoid retain cycles when using this class.

## Topics

### Activating the Manager
- [func activate(completionHandler: ENErrorHandler)](enmanager/activate(completionhandler:).md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [typealias ENActivityHandler](enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ENErrorHandler)](enmanager/setexposurenotificationenabled(_:completionhandler:).md)
  Enables or disables exposure notification.
### Obtaining Exposure Information
- [func detectExposures(configuration: ENExposureConfiguration, diagnosisKeyURLs: [URL], completionHandler: ENDetectExposuresHandler) -> Progress](enmanager/detectexposures(configuration:diagnosiskeyurls:completionhandler:).md)
  Detects exposures using the configuration that you specify for controlling the scoring algorithm.
- [func detectExposures(configuration: ENExposureConfiguration, completionHandler: ENDetectExposuresHandler) -> Progress](enmanager/detectexposures(configuration:completionhandler:).md)
  Detects exposures using the specified configuration to control the scoring algorithm.
- [func getExposureWindows(summary: ENExposureDetectionSummary, completionHandler: ENGetExposureWindowsHandler) -> Progress](enmanager/getexposurewindows(summary:completionhandler:).md)
  Obtains information from the provided summary about the user’s exposure within a window of time.
- [typealias ENGetExposureWindowsHandler](engetexposurewindowshandler.md)
  The handler the system invokes when the acquisition of windows completes.
- [func getUserTraveled(completionHandler: ENGetUserTraveledHandler)](enmanager/getusertraveled(completionhandler:).md)
  Obtains information about the user’s travel within an exposure period.
- [typealias ENGetUserTraveledHandler](engetusertraveledhandler.md)
  The handler the system invokes when acquistiion of the user’s travel status completes.
- [func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: ENGetExposureInfoHandler) -> Progress](enmanager/getexposureinfo(summary:userexplanation:completionhandler:).md)
  Returns information about each exposure.
### Obtaining Exposure Keys
- [func getDiagnosisKeys(completionHandler: ENGetDiagnosisKeysHandler)](enmanager/getdiagnosiskeys(completionhandler:).md)
  Requests the temporary exposure keys from the user’s device to share with a server.
- [func getTestDiagnosisKeys(completionHandler: ENGetDiagnosisKeysHandler)](enmanager/gettestdiagnosiskeys(completionhandler:).md)
  Requests the temporary exposure keys, including the current key, used by this device for testing.
- [class ENTemporaryExposureKey](entemporaryexposurekey.md)
  The key used to generate rolling proximity identifiers.
### Configuring the Manager
- [var exposureNotificationStatus: ENStatus](enmanager/exposurenotificationstatus.md)
  A property that indicates the status of exposure notifications.
- [var exposureNotificationEnabled: Bool](enmanager/exposurenotificationenabled.md)
  A property that indicates that a user enabled exposure notification.
- [class var authorizationStatus: ENAuthorizationStatus](enmanager/authorizationstatus.md)
  A property that reports the current authorization status of the app, and never prompts the user.
- [var dispatchQueue: dispatch_queue_t](enmanager/dispatchqueue.md)
  The dispatch queue on which to invoke handlers.
### Preauthorizing Exposure Keys
- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ENErrorHandler)](enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:).md)
  Requests diagnosis keys after the user authorizes sharing them.
- [func preAuthorizeDiagnosisKeys(completionHandler: ENErrorHandler)](enmanager/preauthorizediagnosiskeys(completionhandler:).md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [typealias ENDiagnosisKeysAvailableHandler](endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](enmanager/diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.
### Invalidating the Manager
- [func invalidate()](enmanager/invalidate.md)
  Stops any outstanding operations and invalidates the manager.
### Instance Properties
- [var invalidationHandler: (() -> Void)?](enmanager/invalidationhandler.md)
  The handler that the framework invokes when invalidation completes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting Exposure Notifications Express](supporting-exposure-notifications-express.md)
  Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](building-an-app-to-notify-users-of-covid-19-exposure.md)
  Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](setting-up-a-key-server.md)
  Ensure that your server meets the requirements for supporting Exposure Notifications.
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

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager)*