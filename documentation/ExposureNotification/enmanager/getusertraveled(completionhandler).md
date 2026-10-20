# getUserTraveled(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method  
**Role**: Instance Method

Obtains information about the user’s travel within an exposure period.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func getUserTraveled(completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func userTraveled() async throws -> Bool
```

```objc
- (void) getUserTraveledWithCompletionHandler:(ENGetUserTraveledHandler) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func userTraveled() async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

Use this method to determine whether the user has traveled outside of the region associated with your app anytime in the last 14 days. You might use this information to determine when to share keys across regions. The first time you use this method, the user will be asked for permission. The app must be in the foreground the first time this is called so that the app may ask the user for permission.

## Parameters

- `completionHandler`: The completion handler that the framework calls when the method completes.

## See Also

### Obtaining Exposure Information
- [func detectExposures(configuration: ENExposureConfiguration, diagnosisKeyURLs: [URL], completionHandler: ENDetectExposuresHandler) -> Progress](./detectexposures%28configuration,diagnosiskeyurls,completionhandler%29.md)
  Detects exposures using the configuration that you specify for controlling the scoring algorithm.
- [func detectExposures(configuration: ENExposureConfiguration, completionHandler: ENDetectExposuresHandler) -> Progress](./detectexposures%28configuration,completionhandler%29.md)
  Detects exposures using the specified configuration to control the scoring algorithm.
- [func getExposureWindows(summary: ENExposureDetectionSummary, completionHandler: ENGetExposureWindowsHandler) -> Progress](./getexposurewindows%28summary,completionhandler%29.md)
  Obtains information from the provided summary about the user’s exposure within a window of time.
- [typealias ENGetExposureWindowsHandler](../engetexposurewindowshandler.md)
  The handler the system invokes when the acquisition of windows completes.
- [typealias ENGetUserTraveledHandler](../engetusertraveledhandler.md)
  The handler the system invokes when acquistiion of the user’s travel status completes.
- [func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: ENGetExposureInfoHandler) -> Progress](./getexposureinfo%28summary,userexplanation,completionhandler%29.md)
  Returns information about each exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/getusertraveled(completionhandler:))*