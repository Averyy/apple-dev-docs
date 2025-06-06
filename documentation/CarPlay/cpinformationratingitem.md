# CPInformationRatingItem

**Framework**: CarPlay  
**Kind**: class

A data object that provides rated content for an information template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPInformationRatingItem
```

#### Overview

`CPInformationRatingItem` provides the ability to display rated content in the rows of an information template. Depending on the template’s layout, the item’s attributes stack vertically or horizontally in the rows. The [`title`](cpinformationitem/title.md) property describes the content, and the [`detail`](cpinformationitem/detail.md) property provides the content. Use the [`rating`](cpinformationratingitem/rating.md) and [`maximumRating`](cpinformationratingitem/maximumrating.md) properties to display a rating for the content. For example, you could show a service rating when displaying information about a restaurant or café.

The template manages the visual styling of the rating and maximum rating.

## Topics

### Creating a Rating Item
- [init(rating: NSNumber?, maximumRating: NSNumber?, title: String?, detail: String?)](cpinformationratingitem/init(rating:maximumrating:title:detail:).md)
  Creates a rating item with a current and a maximum rating.
### Accessing the Item’s Attributes
- [var rating: NSNumber?](cpinformationratingitem/rating.md)
  The current rating that the template displays.
- [var maximumRating: NSNumber?](cpinformationratingitem/maximumrating.md)
  The maximum rating that the template displays.

## Relationships

### Inherits From
- [CPInformationItem](cpinformationitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var items: [CPInformationItem]](cpinformationtemplate/items.md)
  The items that the template displays.
- [class CPInformationItem](cpinformationitem.md)
  A data object that provides content for an information template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationratingitem)*