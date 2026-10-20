# SCCaptureDynamicRange

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Specifies whether the captured screen output is standard or high dynamic range.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 15.0+

## Declaration

```swift
enum SCCaptureDynamicRange
```

```c
enum SCCaptureDynamicRange : NSInteger;
```

#### Overview

High dynamic range screenshot capture may specify local or canonical display attributes optimizing output for presentation on either the capture display or any high dyanmic range display. The screenshot capture updates the output screen capture buffer pixel format and color space to support high dynamic range when specified.

## Topics

### Enumeration Cases
- [SCCaptureDynamicRange.SDR](./sccapturedynamicrange/sdr.md)
  Specifies that the system captures the screen in standard dynamic range.
- [SCCaptureDynamicRange.hdrCanonicalDisplay](./sccapturedynamicrange/hdrcanonicaldisplay.md)
  Specifies that the system captures the screen in high dynamic range with attributes of the canonical display.
- [SCCaptureDynamicRange.hdrLocalDisplay](./sccapturedynamicrange/hdrlocaldisplay.md)
  Specifies that the system captures the screen in high dynamic range with attributes of the local display.
### Initializers
- [init?(rawValue: Int)](./sccapturedynamicrange/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [SCStreamConfiguration.Preset](./scstreamconfiguration/preset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccapturedynamicrange)*