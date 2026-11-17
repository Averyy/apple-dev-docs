# CPSelectableListItem

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

An interface for responding to selections in list items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPSelectableListItem : CPListTemplateItem
```

```objc
@protocol CPSelectableListItem <CPListTemplateItem>
```

## Overview

This protocol provides system-provided list item types with the support they need to handle interactions. Don’t add this protocol directly to your custom types. Instead, use it through a system type such as [`CPListItem`](./cplistitem.md) or [`CPListImageRowItem`](./cplistimagerowitem.md).

## Topics

### Responding to a selection
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./cpselectablelistitem/handler.md)
  The closure to run when someone interacts with any part of the item.

## Relationships

### Inherits From
- [CPListTemplateItem](./cplisttemplateitem.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [CPListImageRowItem](./cplistimagerowitem.md)
- [CPListItem](./cplistitem.md)

## See Also

### Common types
- [class CPThumbnailImage](./cpthumbnailimage.md)
  An image that can display overlays and metadata on top of the image.
- [class CPListImageRowItemElement](./cplistimagerowitemelement.md)
  An abstract class for an element in a row of a list.
- [protocol CPListTemplateItem](./cplisttemplateitem.md)
  An interface that describes the common properties of all list item types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpselectablelistitem)*