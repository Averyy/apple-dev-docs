# hasPlayedToEnd

**Framework**: TV Services  
**Kind**: property

A Boolean value indicating whether the user can be considered to have finished this item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@NSCopying
var hasPlayedToEnd: NSNumber? { get set }
```

#### Discussion

The number of this property is interpreted as a Boolean value.

## See Also

- [var currentPosition: NSNumber?](tvcontentitem/currentposition.md)
  The index location, measured in seconds, at which the user last played this item.
- [var lastAccessedDate: Date?](tvcontentitem/lastaccesseddate.md)
  The date when the user last accessed this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/hasplayedtoend)*