# ENGetUserTraveledHandler

**Framework**: Exposure Notification  
**Kind**: typealias

The handler the system invokes when acquistiion of the user’s travel status completes.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
typealias ENGetUserTraveledHandler = (Bool, (any Error)?) -> Void
```

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.5 and later.

 This type is available in iOS 12.5, and in iOS 13.5 and later.

## Parameters

- `traveled`: Indicates whether the user has traveled.
- `error`: A successful invocation if  ; otherwise, the error that occured.

## See Also

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
- [func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: ENGetExposureInfoHandler) -> Progress](enmanager/getexposureinfo(summary:userexplanation:completionhandler:).md)
  Returns information about each exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/engetusertraveledhandler)*