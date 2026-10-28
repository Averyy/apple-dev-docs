# isStudioLightSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format supports Studio Light.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var isStudioLightSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStudioLightSupported) BOOL studioLightSupported;
```

## Discussion

See [`isStudioLightEnabled`](../isstudiolightenabled.md) for more information on the Studio Light feature.

## See Also

### Determining Studio Light support
- [var videoFrameRateRangeForStudioLight: AVFrameRateRange?](./videoframeraterangeforstudiolight.md)
  A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isstudiolightsupported)*