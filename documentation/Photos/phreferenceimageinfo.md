# PHReferenceImageInfo

**Framework**: Photos  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class PHReferenceImageInfo
```

## Topics

### Initializers
- [init(asset: PHAsset)](./phreferenceimageinfo/init%28asset%29.md)
  Creates a Apple Reference Image info object from a PHAsset representing a photo from the photo library.
- [init(fileURL: URL)](./phreferenceimageinfo/init%28fileurl%29.md)
  Creates an info object from a file URL representing a HEIC, JPEG, or DNG containing an image with Apple Reference Image data.
### Instance Properties
- [var imageContainsReferenceImageData: Bool](./phreferenceimageinfo/imagecontainsreferenceimagedata.md)
  Returns true if the file or photo library asset used to construct this object contains Apple Reference Image data.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phreferenceimageinfo)*