# getExposureWindows(summary:completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method  
**Role**: Instance Method

Obtains information from the provided summary about the user’s exposure within a window of time.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func getExposureWindows(summary: ENExposureDetectionSummary, completionHandler: @escaping ENGetExposureWindowsHandler) -> Progress
```

```objc
- (NSProgress *) getExposureWindowsFromSummary:(ENExposureDetectionSummary *) summary completionHandler:(ENGetExposureWindowsHandler) completionHandler;
```

## Return Value

The progress of the method.

## Discussion

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

Use this method to retrieve summary data about the user’s potential exposure within different time windows. This method will only provide information when your app’s `Info.plist` file has `ENAPIVersion` set to `2`.

## Parameters

- `summary`: The summary of exposure detections.
- `completionHandler`: The completion handler that the framework calls when the method completes.

## See Also

### Obtaining Exposure Information
- [func detectExposures(configuration: ENExposureConfiguration, diagnosisKeyURLs: [URL], completionHandler: ENDetectExposuresHandler) -> Progress](./detectexposures%28configuration,diagnosiskeyurls,completionhandler%29.md)
  Detects exposures using the configuration that you specify for controlling the scoring algorithm.
- [func detectExposures(configuration: ENExposureConfiguration, completionHandler: ENDetectExposuresHandler) -> Progress](./detectexposures%28configuration,completionhandler%29.md)
  Detects exposures using the specified configuration to control the scoring algorithm.
- [typealias ENGetExposureWindowsHandler](../engetexposurewindowshandler.md)
  The handler the system invokes when the acquisition of windows completes.
- [func getUserTraveled(completionHandler: (Bool, (any Error)?) -> Void)](./getusertraveled%28completionhandler%29.md)
  Obtains information about the user’s travel within an exposure period.
- [typealias ENGetUserTraveledHandler](../engetusertraveledhandler.md)
  The handler the system invokes when acquistiion of the user’s travel status completes.
- [func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: ENGetExposureInfoHandler) -> Progress](./getexposureinfo%28summary,userexplanation,completionhandler%29.md)
  Returns information about each exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/getexposurewindows(summary:completionhandler:))*