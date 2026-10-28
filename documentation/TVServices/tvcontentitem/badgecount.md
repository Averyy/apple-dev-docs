# badgeCount

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

A badging integer for this item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
@NSCopying
var badgeCount: NSNumber? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSNumber * badgeCount;
```

## Discussion

The display-badge number is interpreted as a positive integer. Not all UI elements that use content items display badges.

## See Also

### Inspecting the General Display Properties
- [var title: String?](./title.md)
  The localized string title of the item.
- [var topShelfItems: [TVContentItem]?](./topshelfitems.md)
  An array of content items that are the items of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/badgecount)*