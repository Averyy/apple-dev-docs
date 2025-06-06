# MAFlashingLightsProcessor.Result

**Framework**: Media Accessibility  
**Kind**: struct

An object that reports the result of the flashing lights processor.

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
struct Result
```

#### Overview

An [`MAFlashingLightsProcessor.Result`](maflashinglightsprocessor/result.md) object is the result of calling [`processSurface(_:outSurface:timestamp:options:)`](maflashinglightsprocessor/processsurface(_:outsurface:timestamp:options:).md). This object indicates whether the method successfully processed the input surface, the intensity of flashing lights in the input surface, and the amount of mitigation in the output surface.

## Topics

### Interpreting results from video processing
- [var surfaceProcessed: Bool](maflashinglightsprocessor/result/surfaceprocessed.md)
  A Boolean value that indicates whether the flashing lights processor successfully processed the input surface.
- [var intensityLevel: Float](maflashinglightsprocessor/result/intensitylevel.md)
  The intensity of flashing lights in the input surface.
- [var mitigationLevel: Float](maflashinglightsprocessor/result/mitigationlevel.md)
  The amount of mitigation in the output surface.

## See Also

- [func processSurface(IOSurfaceRef, outSurface: inout IOSurfaceRef, timestamp: CFAbsoluteTime, options: [MAFlashingLightsProcessor.OptionKey : Any]?) -> MAFlashingLightsProcessor.Result](maflashinglightsprocessor/processsurface(_:outsurface:timestamp:options:).md)
  Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.
- [MAFlashingLightsProcessor.OptionKey](maflashinglightsprocessor/optionkey.md)
  Options for the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/result)*