# NSTextAttachment

**Framework**: AppKit  
**Kind**: class

The values for the attachment characteristics of attributed strings and related objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSTextAttachment
```

#### Overview

The [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) class uses text attachment objects as the values for attachment attributes (stored in the attributed string under the [`attachment`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/attachment) key).

A text attachment object contains either an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object or an [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object, which in turn holds the contents of the attached file. The properties of this class configure the appearance of the text attachment in your interface. In macOS, the text attachment also uses a cell object that conforms to the [`NSTextAttachmentCellProtocol`](nstextattachmentcellprotocol.md) protocol to draw the image that represents the text and handles mouse events. For more information about text attachments, see the [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) and [`NSTextView`](nstextview.md).

In macOS 12 and iOS 15 and later, [`NSTextAttachmentViewProvider`](nstextattachmentviewprovider.md) and [`NSTextAttachmentLayout`](nstextattachmentlayout.md) provide additional capabilities to represent document locations in terms of an [`NSTextLocation`](nstextlocation.md) or an [`NSTextRange`](nstextrange.md), and provide support for view-based text attachments.

## Topics

### Initializing a text attachment
- [convenience init(fileWrapper: FileWrapper?)](nstextattachment/init(filewrapper:).md)
  Creates a text attachment object to contain the specified file wrapper.
- [init(data: Data?, ofType: String?)](nstextattachment/init(data:oftype:).md)
  Creates a text attachment object with the specified data.
### Defining the attachment’s contents
- [var bounds: CGRect](nstextattachment/bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](nstextattachment/contents.md)
  The contents for the text attachment.
- [var fileType: String?](nstextattachment/filetype.md)
  The file type of the contents for the text attachment.
- [var image: NSImage?](nstextattachment/image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var fileWrapper: FileWrapper?](nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](nstextattachment/allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](nstextattachment/usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](nstextattachment/linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.
### Setting the attachment cell
- [var attachmentCell: (any NSTextAttachmentCellProtocol)?](nstextattachment/attachmentcell.md)
  The object that draws the icon for the text attachment and handles mouse events.
### Constants
- [Attachment Character](attachment-character.md)
  A character that denotes an attachment.
### Convenience methods
- [class func registerViewProviderClass(AnyClass, forFileType: String)](nstextattachment/registerviewproviderclass(_:forfiletype:).md)
  Registers a specific file type with the attachment view provider.
- [class func textAttachmentViewProviderClass(forFileType: String) -> AnyClass?](nstextattachment/textattachmentviewproviderclass(forfiletype:).md)
  Returns the text attachment view provider class, if any, for the file type you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTextAttachmentContainer](nstextattachmentcontainer.md)
- [NSTextAttachmentLayout](nstextattachmentlayout.md)

## See Also

- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [class NSAdaptiveImageGlyph](nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [class NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.
- [protocol NSTextAttachmentCellProtocol](nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment)*