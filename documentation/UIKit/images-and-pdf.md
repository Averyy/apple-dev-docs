# Images and PDF

**Framework**: UIKit

Create and manage images, including those that use bitmap and PDF formats.

## Topics

### Representations
- [class UIImage](uiimage.md)
  An object that manages image data in your app.
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
### Image creation
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
- [func UIGraphicsEndImageContext()](uigraphicsendimagecontext().md)
  Removes the current bitmap-based graphics context from the top of the stack.
### Photo album
- [func UIImageWriteToSavedPhotosAlbum(UIImage, Any?, Selector?, UnsafeMutableRawPointer?)](uiimagewritetosavedphotosalbum(_:_:_:_:).md)
  Adds the specified image to the user’s Camera Roll album.
- [func UISaveVideoAtPathToSavedPhotosAlbum(String, Any?, Selector?, UnsafeMutableRawPointer?)](uisavevideoatpathtosavedphotosalbum(_:_:_:_:).md)
  Adds the movie from the specified path to the user’s Camera Roll album.
- [func UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(String) -> Bool](uivideoatpathiscompatiblewithsavedphotosalbum(_:).md)
  Returns a Boolean value that indicates whether the specified video is compatible to save to the user’s Camera Roll album.
### PDF creation
- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfcontexttodata(_:_:_:).md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](uigraphicsbeginpdfcontexttofile(_:_:_:).md)
  Creates a PDF graphics context that targets a file at the specified path.
- [func UIGraphicsEndPDFContext()](uigraphicsendpdfcontext().md)
  Closes a PDF graphics context and pops it from the current context stack.
- [func UIGraphicsBeginPDFPage()](uigraphicsbeginpdfpage().md)
  Marks the beginning of a new page in a PDF context and configures it using default values.
- [func UIGraphicsBeginPDFPageWithInfo(CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfpagewithinfo(_:_:).md)
  Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [func UIGraphicsGetPDFContextBounds() -> CGRect](uigraphicsgetpdfcontextbounds().md)
  Returns the current page bounds.
- [func UIGraphicsAddPDFContextDestinationAtPoint(String, CGPoint)](uigraphicsaddpdfcontextdestinationatpoint(_:_:).md)
  Creates a jump destination in the current page.
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](uigraphicssetpdfcontextdestinationforrect(_:_:).md)
  Links a rectangular area on the current page to the specified jump destination.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.
### PDF screenshots
- [class UIScreenshotService](uiscreenshotservice.md)
  An object that coordinates the creation of PDF screenshots of an app’s content.

## See Also

- [Drawing](drawing.md)
  Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.
- [Printing](printing.md)
  Display the system print panels and manage the printing process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/images-and-pdf)*