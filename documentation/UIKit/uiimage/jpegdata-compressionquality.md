# jpegData(compressionQuality:)

**Framework**: UIKit  
**Kind**: method

Returns a data object that contains the image in JPEG format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func jpegData(compressionQuality: CGFloat) -> Data?
```

#### Return Value

A data object containing the JPEG data, or `nil` if there’s a problem generating the data. This function may return `nil` if the image has no data or if the underlying `CGImageRef` contains data in an unsupported bitmap format.

#### Discussion

If the image object’s underlying image data has been purged, calling this function forces that data to be reloaded into memory.

## Parameters

- `compressionQuality`: The quality of the resulting JPEG image, expressed as a value from   to  . The value   represents the maximum compression (or lowest quality) while the value   represents the least compression (or best quality).

## See Also

- [Supporting HDR images in your app](supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [func pngData() -> Data?](uiimage/pngdata.md)
  Returns a data object that contains the specified image in PNG format.
- [func UIGraphicsBeginImageContext(CGSize)](uigraphicsbeginimagecontext(_:).md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](uigraphicsgetimagefromcurrentimagecontext().md)
  Returns an image from the contents of the current bitmap-based graphics context.
- [func UIGraphicsEndImageContext()](uigraphicsendimagecontext().md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/jpegdata(compressionquality:))*