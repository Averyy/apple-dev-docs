# pngData()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a data object that contains the specified image in PNG format.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
func pngData() -> Data?
```

```c
extern NSData *UIImagePNGRepresentation(UIImage *image);
```

#### Return Value

A data object containing the PNG data, or `nil` if there was a problem generating the data. This function may return `nil` if the image has no data or if the underlying `CGImageRef` contains data in an unsupported bitmap format.

#### Discussion

If the image object’s underlying image data has been purged, calling this function forces that data to be reloaded into memory.

## See Also

### Image creation
- [Supporting HDR images in your app](../supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [func jpegData(compressionQuality: CGFloat) -> Data?](./jpegdata%28compressionquality%29.md)
  Returns a data object that contains the image in JPEG format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/pngdata())*