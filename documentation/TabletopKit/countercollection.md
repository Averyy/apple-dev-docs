# CounterCollection

**Framework**: TabletopKit  
**Kind**: struct

A collection of score counters that can be inspected and modified.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CounterCollection
```

## Topics

### Instance Properties
- [var count: Int](countercollection/count.md)
  The number of score counters.
- [var ids: [ScoreCounter.ID]](countercollection/ids.md)
  The identifiers of the score counters.
### Subscripts
- [subscript(ScoreCounter.ID) -> Int64?](countercollection/subscript(_:).md)
  Queries or modifies the value of the score counter with given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/countercollection)*