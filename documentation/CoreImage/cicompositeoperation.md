# CICompositeOperation

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a composite operation filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CICompositeOperation : CIFilterProtocol
```

```objc
@protocol CICompositeOperation <CIFilter>
```

## Topics

### Instance Properties
- [var backgroundImage: CIImage?](./cicompositeoperation/backgroundimage.md)
  The image to use as a background image.
- [var inputImage: CIImage?](./cicompositeoperation/inputimage.md)
  The image to use as a foreground image.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [Composite Operations](./composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicompositeoperation)*