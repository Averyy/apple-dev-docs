# CMSyncMightDrift(_:_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether it’s possible for one timebase or clock to drift relative to the other.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSyncMightDrift(_ clockOrTimebase1: CMClockOrTimebase, _ clockOrTimebase2: CMClockOrTimebase) -> Bool
```

#### Discussion

A timebase can drift relative to another if they are ultimately mastered by clocks that can drift relative to each other.

## See Also

- [func CMClockMightDrift(CMClock, otherClock: CMClock) -> Bool](cmclockmightdrift(_:otherclock:).md)
  Returns a Boolean value that indicates whether it’s possible for two clocks to drift relative to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncmightdrift(_:_:))*