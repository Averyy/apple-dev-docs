# CMClockMightDrift(_:otherClock:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether it’s possible for two clocks to drift relative to each other.

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
func CMClockMightDrift(_ clock: CMClock, otherClock: CMClock) -> Bool
```

## Parameters

- `clock`: The first clock to compare.
- `otherClock`: The second clock to compare.

## See Also

- [func CMSyncMightDrift(CMClockOrTimebase, CMClockOrTimebase) -> Bool](cmsyncmightdrift(_:_:).md)
  Returns a Boolean value that indicates whether it’s possible for one timebase or clock to drift relative to the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockmightdrift(_:otherclock:))*