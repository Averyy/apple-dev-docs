# lastAccessedDate

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The date when the user last accessed this item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
var lastAccessedDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * lastAccessedDate;
```

## Discussion

A typical use is for content types in which “playing” represents the date when the user last played the item or played a subitem within the group. When the user simply looks at an item, the access date should not change.

## See Also

### Inspecting the Playback Properties
- [var currentPosition: NSNumber?](./currentposition.md)
  The index location, measured in seconds, at which the user last played this item.
- [var hasPlayedToEnd: NSNumber?](./hasplayedtoend.md)
  A Boolean value indicating whether the user can be considered to have finished this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/lastaccesseddate)*