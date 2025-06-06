# processSurface(_:outSurface:timestamp:options:)

**Framework**: Media Accessibility  
**Kind**: method

Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func processSurface(_ inSurface: IOSurfaceRef, outSurface: inout IOSurfaceRef, timestamp: CFAbsoluteTime, options: [MAFlashingLightsProcessor.OptionKey : Any]? = nil) -> MAFlashingLightsProcessor.Result
```

#### Return Value

An [`MAFlashingLightsProcessor.Result`](maflashinglightsprocessor/result.md) object that indicates whether the processor successfully processed the input surface, the intensity of flashing lights in the input surface, and the amount of mitigation in the output surface.

## Parameters

- `inSurface`: The input   to process for flashing lights.
- `outSurface`: The output   for storing the mitigated video frame. This is the surface to display to the user.
- `timestamp`: The time when your app displays the video frame to the user. The flashing lights processor uses the timestamp to determine the video’s real-time frame rate for the detection algorithm.
- `options`: An options dictionary for additional parameters.

## See Also

- [MAFlashingLightsProcessor.Result](maflashinglightsprocessor/result.md)
  An object that reports the result of the flashing lights processor.
- [MAFlashingLightsProcessor.OptionKey](maflashinglightsprocessor/optionkey.md)
  Options for the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/processsurface(_:outsurface:timestamp:options:))*