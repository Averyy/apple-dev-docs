# processSurface:outSurface:timestamp:options:

**Framework**: Media Accessibility  
**Kind**: method  
**Role**: Instance Method

Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (MAFlashingLightsProcessorResult *) processSurface:(IOSurfaceRef) inSurface outSurface:(IOSurfaceRef) outSurface timestamp:(CFAbsoluteTime) timestamp options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

An [`MAFlashingLightsProcessorResult`](../maflashinglightsprocessorresult.md) object that indicates whether the processor successfully processed the input surface, the intensity of flashing lights in the input surface, and the amount of mitigation in the output surface.

## Parameters

- `inSurface`: The input [`IOSurfaceRef`](../../IOSurface/iosurfaceref.md) to process for flashing lights.
- `outSurface`: The output [`IOSurfaceRef`](../../IOSurface/iosurfaceref.md) for storing the mitigated video frame. This is the surface to display to the user.
- `timestamp`: The time when your app displays the video frame to the user. The flashing lights processor uses the timestamp to determine the video’s real-time frame rate for the detection algorithm.
- `options`: An options dictionary for additional parameters.

## See Also

### Processing video content
- [MAFlashingLightsProcessorResult](../maflashinglightsprocessorresult.md)
  An object that reports the result of the flashing lights processor.
- [MAFlashingLightsProcessor.OptionKey](./optionkey.md)
  Options for the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/processsurface:outsurface:timestamp:options:)*