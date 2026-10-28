# ENGetUserTraveledHandler

**Framework**: Exposure Notification  
**Kind**: typealias  
**Role**: Type Alias

The handler the system invokes when acquistiion of the user’s travel status completes.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
typealias ENGetUserTraveledHandler = (Bool, (any Error)?) -> Void
```

```c
typedef void (^)(_Bool, NSError *) ENGetUserTraveledHandler;
```

## Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.5 and later.

## Parameters

- `traveled`: Indicates whether the user has traveled.
- `error`: A successful invocation if `nil`; otherwise, the error that occured.

## See Also

### Obtaining Exposure Information
- [func detectExposures(configuration: ENExposureConfiguration, diagnosisKeyURLs: [URL], completionHandler: ENDetectExposuresHandler) -> Progress](./enmanager/detectexposures%28configuration,diagnosiskeyurls,completionhandler%29.md)
  Detects exposures using the configuration that you specify for controlling the scoring algorithm.
- [func detectExposures(configuration: ENExposureConfiguration, completionHandler: ENDetectExposuresHandler) -> Progress](./enmanager/detectexposures%28configuration,completionhandler%29.md)
  Detects exposures using the specified configuration to control the scoring algorithm.
- [func getExposureWindows(summary: ENExposureDetectionSummary, completionHandler: ENGetExposureWindowsHandler) -> Progress](./enmanager/getexposurewindows%28summary,completionhandler%29.md)
  Obtains information from the provided summary about the user’s exposure within a window of time.
- [typealias ENGetExposureWindowsHandler](./engetexposurewindowshandler.md)
  The handler the system invokes when the acquisition of windows completes.
- [func getUserTraveled(completionHandler: (Bool, (any Error)?) -> Void)](./enmanager/getusertraveled%28completionhandler%29.md)
  Obtains information about the user’s travel within an exposure period.
- [func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: ENGetExposureInfoHandler) -> Progress](./enmanager/getexposureinfo%28summary,userexplanation,completionhandler%29.md)
  Returns information about each exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/engetusertraveledhandler)*