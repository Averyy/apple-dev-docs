# CISharpenLuminance

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a sharpen luminance filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CISharpenLuminance : CIFilterProtocol
```

```objc
@protocol CISharpenLuminance <CIFilter>
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](./cisharpenluminance/inputimage.md)
  The image to use as an input image.
- [var radius: Float](./cisharpenluminance/radius.md)
  The distance from the center of the effect.
- [var sharpness: Float](./cisharpenluminance/sharpness.md)
  The amount of sharpening to apply.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [class func sharpenLuminance() -> any CIFilter & CISharpenLuminance](./cifilter-swift.class/sharpenluminance%28%29.md)
  Applies a sharpening effect to an image.
### Protocols
- [protocol CIUnsharpMask](./ciunsharpmask.md)
  The properties you use to configure an unsharp mask filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisharpenluminance)*