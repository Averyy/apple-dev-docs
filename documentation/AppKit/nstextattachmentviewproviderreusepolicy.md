# NSTextAttachmentViewProviderReusePolicy

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct NSTextAttachmentViewProviderReusePolicy
```

```c
enum NSTextAttachmentViewProviderReusePolicy : NSUInteger;
```

## Topics

### Creating a reuse policy
- [init(rawValue: UInt)](./nstextattachmentviewproviderreusepolicy/init%28rawvalue%29.md)
### Specifying reuse policy options
- [static var onScrollingOutOfViewport: NSTextAttachmentViewProviderReusePolicy](./nstextattachmentviewproviderreusepolicy/onscrollingoutofviewport.md)
- [static var onEditingInlineParagraphs: NSTextAttachmentViewProviderReusePolicy](./nstextattachmentviewproviderreusepolicy/oneditinginlineparagraphs.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Attachments
- [class NSTextAttachment](./nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](./nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [class NSAdaptiveImageGlyph](./nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](./nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](./nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [class NSTextAttachmentCell](./nstextattachmentcell-swift.class.md)
  An object that implements the functionality of the text attachment cell protocol.
- [protocol NSTextAttachmentCellProtocol](./nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentviewproviderreusepolicy)*