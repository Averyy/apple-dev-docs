# hasPlayedToEnd

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user can be considered to have finished this item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
@NSCopying
var hasPlayedToEnd: NSNumber? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSNumber * hasPlayedToEnd;
```

## Discussion

The number of this property is interpreted as a Boolean value.

## See Also

### Inspecting the Playback Properties
- [var currentPosition: NSNumber?](./currentposition.md)
  The index location, measured in seconds, at which the user last played this item.
- [var lastAccessedDate: Date?](./lastaccesseddate.md)
  The date when the user last accessed this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/hasplayedtoend)*