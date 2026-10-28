# NSTextAttachmentCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that implements the functionality of the text attachment cell protocol.

**Availability**:
- macOS

## Declaration

```swift
class NSTextAttachmentCell
```

```objc
@interface NSTextAttachmentCell : NSCell
```

## Overview

This specification describes only those methods whose implementations have features that are particular to this class. For a general discussion of the protocol’s methods, see [`NSTextAttachmentCellProtocol`](./nstextattachmentcellprotocol.md).

## Relationships

### Inherits From
- [NSCell](./nscell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextAttachmentCellProtocol](./nstextattachmentcellprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [Text Attachment Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttachments/TextAttachments.html#//apple_ref/doc/uid/10000094i)
### Attachments
- [class NSTextAttachment](./nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](./nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [struct NSTextAttachmentViewProviderReusePolicy](./nstextattachmentviewproviderreusepolicy.md)
- [class NSAdaptiveImageGlyph](./nsadaptiveimageglyph.md)
  A data object for an emoji-like image that can appear in attributed text.
- [protocol NSTextAttachmentContainer](./nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](./nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.
- [protocol NSTextAttachmentCellProtocol](./nstextattachmentcellprotocol.md)
  A set of methods that declares the interface for objects that draw text attachment icons and handle mouse events on their icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcell-swift.class)*