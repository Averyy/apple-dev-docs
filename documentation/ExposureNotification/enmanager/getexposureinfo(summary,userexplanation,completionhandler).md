# getExposureInfo(summary:userExplanation:completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method  
**Role**: Instance Method

Returns information about each exposure.

**Availability**:
- iOS 13.5+ - Deprecated in 13.6
- iPadOS 13.5+ - Deprecated in 13.6
- Mac Catalyst 13.5+ - Deprecated in 13.6

> **Deprecated**: Use getExposureWindowsFromSummary, if needed.

## Declaration

```swift
func getExposureInfo(summary: ENExposureDetectionSummary, userExplanation: String, completionHandler: @escaping ENGetExposureInfoHandler) -> Progress
```

```objc
- (NSProgress *) getExposureInfoFromSummary:(ENExposureDetectionSummary *) summary userExplanation:(NSString *) userExplanation completionHandler:(ENGetExposureInfoHandler) completionHandler;
```

## Return Value

The progress of the method.

## Discussion

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 to 13.6.

Calls to this method generate a user notification that presents the `userExplanation`.

## Parameters

- `summary`: The summary of exposure.
- `userExplanation`: A string that the framework displays to the user informing them of the exposure.
- `completionHandler`: The completion handler that the framework calls when the method completes.

## Topics

### Completion Handlers
- [typealias ENGetExposureInfoHandler](../engetexposureinfohandler.md)
  The definition of a handler that receives exposure info.

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
- [func getUserTraveled(completionHandler: (Bool, (any Error)?) -> Void)](./getusertraveled%28completionhandler%29.md)
  Obtains information about the user’s travel within an exposure period.
- [typealias ENGetUserTraveledHandler](../engetusertraveledhandler.md)
  The handler the system invokes when acquistiion of the user’s travel status completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/getexposureinfo(summary:userexplanation:completionhandler:))*