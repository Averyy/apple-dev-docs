# init(fileURL:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates an info object from a file URL representing a HEIC, JPEG, or DNG containing an image with Apple Reference Image data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
init(fileURL: URL)
```

#### Discussion

If the file URL references a file that is not an image file, or an image file that does not contain Apple Reference Image data, `PHReferenceImageInfo/imageContainsReferenceImageData` will return false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phreferenceimageinfo/init(fileurl:))*