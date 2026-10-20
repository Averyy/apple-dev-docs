# title

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The localized string title of the item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

#### Discussion

The title should be localized into the current user’s locale.

## See Also

### Inspecting the General Display Properties
- [var badgeCount: NSNumber?](./badgecount.md)
  A badging integer for this item.
- [var topShelfItems: [TVContentItem]?](./topshelfitems.md)
  An array of content items that are the items of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/title)*