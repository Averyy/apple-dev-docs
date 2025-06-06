# NSImageDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods that you can use to respond to drawing failures and manage incremental loads.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSImageDelegate : NSObjectProtocol
```

## Topics

### Responding to Drawing Failure
- [func imageDidNotDraw(NSImage, in: NSRect) -> NSImage?](nsimagedelegate/imagedidnotdraw(_:in:).md)
  Tells the delegate that the image object is unable, for whatever reason, to lock focus on its image or draw in the specified rectangle.
### Managing Incremental Loads
- [NSImage.LoadStatus](nsimage/loadstatus.md)
  Status values for incremental image loading.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [class NSImageRep](nsimagerep.md)
  A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagedelegate)*