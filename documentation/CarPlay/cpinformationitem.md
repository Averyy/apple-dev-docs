# CPInformationItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A data object that provides content for an information template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPInformationItem
```

```objc
@interface CPInformationItem : NSObject
```

#### Overview

[`CPInformationTemplate`](./cpinformationtemplate.md) uses information items to populate the rows of its list. Depending on the template’s layout, the item’s [`title`](./cpinformationitem/title.md) and [`detail`](./cpinformationitem/detail.md) values stack vertically or horizontally in the row. Use the `title` property to describe the content, and the `detail` property to provide the content. For example, when using `CPInformationTemplate` to present a food order summary, you could provide an item that displays the number of minutes until the order is ready.

## Topics

### Creating an Information Item
- [init(title: String?, detail: String?)](./cpinformationitem/init%28title,detail%29.md)
  Creates an information item with a title and detail text.
### Accessing the Item’s Attributes
- [var title: String?](./cpinformationitem/title.md)
  The text that the template displays as the item’s title.
- [var detail: String?](./cpinformationitem/detail.md)
  The text that the template displays below or beside the item’s title.
### Initializers
- [init?(coder: NSCoder)](./cpinformationitem/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPInformationRatingItem](./cpinformationratingitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Managing the Items
- [var items: [CPInformationItem]](./cpinformationtemplate/items.md)
  The items that the template displays.
- [class CPInformationRatingItem](./cpinformationratingitem.md)
  A data object that provides rated content for an information template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationitem)*