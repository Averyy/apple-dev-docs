# videoFrameRateRangeForStudioLight

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var videoFrameRateRangeForStudioLight: AVFrameRateRange? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVFrameRateRange * videoFrameRateRangeForStudioLight;
```

## Discussion

Devices may support a limited frame rate range when Studio Light is active. If the format doesn’t support Studio Light, this property is `nil`.

## See Also

### Determining Studio Light support
- [var isStudioLightSupported: Bool](./isstudiolightsupported.md)
  A Boolean value that indicates whether the format supports Studio Light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforstudiolight)*