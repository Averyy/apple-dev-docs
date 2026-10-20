# topShelfItems

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

An array of content items that are the items of a section.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var topShelfItems: [TVContentItem]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<TVContentItem *> * topShelfItems;
```

#### Discussion

If this property is non-`nil`, the content item represents a section item in a sectioned Top Shelf style. For more information, see [`TVTopShelfContentStyle`](../tvtopshelfcontentstyle.md). The title property must also be set to a non-`nil` string.

## See Also

### Inspecting the General Display Properties
- [var badgeCount: NSNumber?](./badgecount.md)
  A badging integer for this item.
- [var title: String?](./title.md)
  The localized string title of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/topshelfitems)*