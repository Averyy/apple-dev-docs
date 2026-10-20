# currentPosition

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The index location, measured in seconds, at which the user last played this item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
@NSCopying
var currentPosition: NSNumber? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSNumber * currentPosition;
```

#### Discussion

The number is interpreted as a double number of seconds.

## See Also

### Inspecting the Playback Properties
- [var hasPlayedToEnd: NSNumber?](./hasplayedtoend.md)
  A Boolean value indicating whether the user can be considered to have finished this item.
- [var lastAccessedDate: Date?](./lastaccesseddate.md)
  The date when the user last accessed this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/currentposition)*