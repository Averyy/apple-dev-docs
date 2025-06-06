# topShelfItems

**Framework**: TV Services  
**Kind**: property

An array of content items that are the items of a section.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var topShelfItems: [TVContentItem]? { get set }
```

#### Discussion

If this property is non-`nil`, the content item represents a section item in a sectioned Top Shelf style. For more information, see [`TVTopShelfContentStyle`](tvtopshelfcontentstyle.md). The title property must also be set to a non-`nil` string.

## See Also

- [var badgeCount: NSNumber?](tvcontentitem/badgecount.md)
  A badging integer for this item.
- [var title: String?](tvcontentitem/title.md)
  The localized string title of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/topshelfitems)*