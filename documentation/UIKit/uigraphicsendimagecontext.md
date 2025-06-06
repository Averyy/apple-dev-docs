# UIGraphicsEndImageContext()

**Framework**: UIKit  
**Kind**: func

Removes the current bitmap-based graphics context from the top of the stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsEndImageContext()
```

#### Discussion

You use this function to clean up the drawing environment put in place by the [`UIGraphicsBeginImageContext(_:)`](uigraphicsbeginimagecontext(_:).md) function and to remove the corresponding bitmap-based graphics context from the top of the stack. If the current context was not created using the [`UIGraphicsBeginImageContext(_:)`](uigraphicsbeginimagecontext(_:).md) function, this function does nothing.

This function may be called from any thread of your app.

## See Also

- [Supporting HDR images in your app](supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [func jpegData(compressionQuality: CGFloat) -> Data?](uiimage/jpegdata(compressionquality:).md)
  Returns a data object that contains the image in JPEG format.
- [func pngData() -> Data?](uiimage/pngdata.md)
  Returns a data object that contains the specified image in PNG format.
- [func UIGraphicsBeginImageContext(CGSize)](uigraphicsbeginimagecontext(_:).md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](uigraphicsgetimagefromcurrentimagecontext().md)
  Returns an image from the contents of the current bitmap-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext())*