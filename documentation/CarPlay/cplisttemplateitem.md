# CPListTemplateItem

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

An interface that describes the common properties of all list item types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPListTemplateItem : NSObjectProtocol
```

```objc
@protocol CPListTemplateItem <NSObject>
```

## Overview

This protocol adds key behaviors to all system-provided list item types. Don’t add this protocol directly to your custom types. Instead, use it through a system type such as [`CPListItem`](./cplistitem.md), [`CPListImageRowItem`](./cplistimagerowitem.md), or [`CPMessageListItem`](./cpmessagelistitem.md).

## Topics

### Managing content
- [var text: String?](./cplisttemplateitem/text.md)
  The primary text to display for the item.
- [var userInfo: Any?](./cplisttemplateitem/userinfo.md)
  App-specific data you associate with the item.
### Enabling items
- [var isEnabled: Bool](./cplisttemplateitem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [CPSelectableListItem](./cpselectablelistitem.md)
### Conforming Types
- [CPListImageRowItem](./cplistimagerowitem.md)
- [CPListItem](./cplistitem.md)
- [CPMessageListItem](./cpmessagelistitem.md)

## See Also

### Common types
- [class CPThumbnailImage](./cpthumbnailimage.md)
  An image that can display overlays and metadata on top of the image.
- [class CPListImageRowItemElement](./cplistimagerowitemelement.md)
  An abstract class for an element in a row of a list.
- [protocol CPSelectableListItem](./cpselectablelistitem.md)
  An interface for responding to selections in list items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplateitem)*