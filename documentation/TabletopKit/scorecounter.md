# ScoreCounter

**Framework**: TabletopKit  
**Kind**: struct

An object that keeps a score in a tabletop game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct ScoreCounter
```

## Topics

### Creating score counters
- [init(id: ScoreCounter.ID, value: Int64)](scorecounter/init(id:value:).md)
  Creates a score counter with a unique identifier and initial value.
### Getting score counter identifiers
- [var id: ScoreCounter.ID](scorecounter/id.md)
  A unique identifier for the score counter.
- [ScoreCounter.Identifier](scorecounter/identifier.md)
  A unique identifier for score counters.
### Getting score counter values
- [var value: Int64](scorecounter/value.md)
  The current value of the score counter.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/scorecounter)*