# CounterCollection

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A collection of score counters that can be inspected and modified.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct CounterCollection
```

## Topics

### Getting the counter details
- [var count: Int](./countercollection/count.md)
  The number of score counters.
- [var ids: [ScoreCounter.ID]](./countercollection/ids.md)
  The identifiers of the score counters.
### Accessing the subscript
- [subscript(ScoreCounter.ID) -> Int64?](./countercollection/subscript%28_%29.md)
  Queries or modifies the value of the score counter with given identifier.

## See Also

### Score counters
- [struct ScoreCounter](./scorecounter.md)
  An object that keeps a score in a tabletop game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/countercollection)*