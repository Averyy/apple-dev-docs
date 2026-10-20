# CIFeatureTypeRectangle

**Framework**: Core Image  
**Kind**: var  
**Role**: Global Variable

A Core Image feature type for rectangular object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
let CIFeatureTypeRectangle: String
```

```c
extern NSString * const CIFeatureTypeRectangle;
```

#### Discussion

To detect rectangles in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [`CIRectangleFeature`](./cirectanglefeature.md) class to find more information about the detected rectangle.

## See Also

### Feature Types
- [let CIFeatureTypeFace: String](./cifeaturetypeface.md)
  A Core Image feature type for person’s face.
- [let CIFeatureTypeQRCode: String](./cifeaturetypeqrcode.md)
  A Core Image feature type for QR code object.
- [let CIFeatureTypeText: String](./cifeaturetypetext.md)
  A Core Image feature type for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)*