# CIFeatureTypeText

**Framework**: Core Image  
**Kind**: var  
**Role**: Global Variable

A Core Image feature type for text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
let CIFeatureTypeText: String
```

```c
extern NSString * const CIFeatureTypeText;
```

#### Discussion

To detect text in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [`CITextFeature`](./citextfeature.md) class to find more information about the detected text.

## See Also

### Feature Types
- [let CIFeatureTypeFace: String](./cifeaturetypeface.md)
  A Core Image feature type for person’s face.
- [let CIFeatureTypeRectangle: String](./cifeaturetyperectangle.md)
  A Core Image feature type for rectangular object.
- [let CIFeatureTypeQRCode: String](./cifeaturetypeqrcode.md)
  A Core Image feature type for QR code object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeaturetypetext)*