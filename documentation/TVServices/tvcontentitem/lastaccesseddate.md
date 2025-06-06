# lastAccessedDate

**Framework**: TV Services  
**Kind**: property

The date when the user last accessed this item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var lastAccessedDate: Date? { get set }
```

#### Discussion

A typical use is for content types in which “playing” represents the date when the user last played the item or played a subitem within the group. When the user simply looks at an item, the access date should not change.

## See Also

- [var currentPosition: NSNumber?](tvcontentitem/currentposition.md)
  The index location, measured in seconds, at which the user last played this item.
- [var hasPlayedToEnd: NSNumber?](tvcontentitem/hasplayedtoend.md)
  A Boolean value indicating whether the user can be considered to have finished this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/lastaccesseddate)*