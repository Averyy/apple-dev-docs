# Images and PDF

**Framework**: AppKit

Create and manage images, in bitmap, PDF, and other formats.

## Topics

### Images
- [Providing images for different appearances](../UIKit/providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../UIKit/supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [Applying Apple HDR effect to your photos](applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
- [class NSImage](nsimage.md)
  A high-level interface for manipulating image data.
- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.
- [class NSImageRep](nsimagerep.md)
  A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.
### Bitmap Formats
- [class NSBitmapImageRep](nsbitmapimagerep.md)
  An object that renders an image from bitmap data.
- [class NSCIImageRep](nsciimagerep.md)
  An object that can render an image from a Core Image object.
- [class NSPICTImageRep](nspictimagerep.md)
  An object that renders an image from a PICT format data stream of version 1, version 2, and extended version 2.
### Vector Formats
- [class NSPDFImageRep](nspdfimagerep.md)
  An object that can render an image from a PDF format data stream.
- [class NSPDFInfo](nspdfinfo.md)
  An object that stores information associated with the creation of a PDF file, such as its URL, tag names, page orientation, and paper size.
- [class NSEPSImageRep](nsepsimagerep.md)
  An object that can render an image from encapsulated PostScript (EPS) code.
### Custom Formats
- [class NSCustomImageRep](nscustomimagerep.md)
  An object that uses a delegate object to render an image from a custom format.

## See Also

- [Drawing](drawing.md)
  Draw shapes, images, and other content on the screen.
- [Color](color.md)
  Represent colors using built-in or custom formats, and give users options for selecting and applying colors.
- [Printing](printing.md)
  Display the system print panels and manage the printing process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/images-and-pdf)*