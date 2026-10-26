# imageContainsReferenceImageData

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Returns true if the file or photo library asset used to construct this object contains Apple Reference Image data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var imageContainsReferenceImageData: Bool { get }
```

#### Discussion

Use this property to determine if the asset contains Apple Reference Image data that can be processed and/or viewed using `View/photosReferenceImageViewer`. If the input was not an image, or does not contain Apple Reference Image data, this returns false.

The first time this property is accessed, the image metadata from the file or from the photo library is read to determine if the image contains Apple Reference Image. Consider wrapping it in a `Task` to avoid blocking the main thread while the image metadata is read.

When this property returns false, you should hide any controls that would show the Apple Reference Image viewer. For example, Preview hides the “Show Reference Image” button in its inspector when viewing an image file that does not contain Apple Reference Image.

visionOS does not support viewing Apple Reference Image data. For iPad apps on visionOS, this property will always return false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phreferenceimageinfo/imagecontainsreferenceimagedata)*