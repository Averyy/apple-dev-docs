# NSImageCell

**Framework**: AppKit  
**Kind**: class

An `NSImageCell` object displays a single image (encapsulated in an [`NSImage`](nsimage.md) object) in a frame. This class provides methods for choosing the frame and for aligning and scaling the image to fit the frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSImageCell
```

#### Overview

The object value of an `NSImageCell` object must be an [`NSImage`](nsimage.md) object, so if you use the [`objectValue`](nscell/objectvalue.md) method of [`NSCell`](nscell.md), be sure to supply an [`NSImage`](nsimage.md) object as an argument. Because an [`NSImage`](nsimage.md) object does not need to be converted for display, do not use the [`NSCell`](nscell.md) methods relating to formatters.

An `NSImageCell` object is usually associated with some kind of control object. For example, an [`NSMatrix`](nsmatrix.md) or an [`NSTableView`](nstableview.md).

##### Designated Initializers

When subclassing `NSImageCell` you must implement all of the designated initializers. Those methods are: init, [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)), [`init(textCell:)`](nscell/init(textcell:).md), and [`init(imageCell:)`](nscell/init(imagecell:).md).

## Topics

### Aligning and Scaling the Image
- [var imageAlignment: NSImageAlignment](nsimagecell/imagealignment.md)
  The alignment of the receiver’s image relative to its frame.
- [var imageScaling: NSImageScaling](nsimagecell/imagescaling.md)
  The scaling mode used to fit the receiver’s image into the frame.
### Choosing the Frame
- [var imageFrameStyle: NSImageView.FrameStyle](nsimagecell/imageframestyle.md)
  The style of the frame that borders the image.
### Constants
- [enum NSImageAlignment](nsimagealignment.md)
  Constants used by [`imageAlignment`](nsimagecell/imagealignment.md) that allow you to specify the location of the image in the frame.
- [NSImageView.FrameStyle](nsimageview/framestyle.md)
  Constants that allow you to specify the kind of frame bordering the image.

## Relationships

### Inherits From
- [NSCell](nscell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagecell)*