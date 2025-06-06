# currentPosition

**Framework**: TV Services  
**Kind**: property

The index location, measured in seconds, at which the user last played this item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@NSCopying
var currentPosition: NSNumber? { get set }
```

#### Discussion

The number is interpreted as a double number of seconds.

## See Also

- [var hasPlayedToEnd: NSNumber?](tvcontentitem/hasplayedtoend.md)
  A Boolean value indicating whether the user can be considered to have finished this item.
- [var lastAccessedDate: Date?](tvcontentitem/lastaccesseddate.md)
  The date when the user last accessed this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/currentposition)*