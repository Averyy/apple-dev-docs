# CMSyncMightDrift(_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CMSyncMightDrift(CMClockOrTimebaseRef clockOrTimebase1, CMClockOrTimebaseRef clockOrTimebase2);
```

#### Discussion

A timebase can drift relative to another if they are ultimately mastered by clocks that can drift relative to each other.

## See Also

### Determining Clock Drift
- [func CMClockMightDrift(CMClock, otherClock: CMClock) -> Bool](./cmclockmightdrift%28_,otherclock%29.md)
  Returns a Boolean value that indicates whether it’s possible for two clocks to drift relative to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncmightdrift(_:_:))*