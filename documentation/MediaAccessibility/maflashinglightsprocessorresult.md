# MAFlashingLightsProcessorResult

**Framework**: Media Accessibility  
**Kind**: class  
**Role**: Class

An object that reports the result of the flashing lights processor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface MAFlashingLightsProcessorResult : NSObject
```

#### Overview

An [`MAFlashingLightsProcessorResult`](./maflashinglightsprocessorresult.md) object is the result of calling [`processSurface:outSurface:timestamp:options:`](./maflashinglightsprocessor/processsurface_outsurface_timestamp_options_.md). This object indicates whether the method successfully processed the input surface, the intensity of flashing lights in the input surface, and the amount of mitigation in the output surface.

## Topics

### Interpreting results from video processing
- [surfaceProcessed](./maflashinglightsprocessorresult/surfaceprocessed.md)
  A Boolean value that indicates whether the flashing lights processor successfully processed the input surface.
- [intensityLevel](./maflashinglightsprocessorresult/intensitylevel.md)
  The intensity of flashing lights in the input surface.
- [mitigationLevel](./maflashinglightsprocessorresult/mitigationlevel.md)
  The amount of mitigation in the output surface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Processing video content
- [- processSurface:outSurface:timestamp:options:](./maflashinglightsprocessor/processsurface_outsurface_timestamp_options_.md)
  Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.
- [MAFlashingLightsProcessor.OptionKey](./maflashinglightsprocessor/optionkey.md)
  Options for the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessorresult)*