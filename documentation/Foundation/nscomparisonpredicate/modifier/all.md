# NSComparisonPredicate.Modifier.all

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A predicate to compare all entries in the destination of a to-many relationship.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case all
```

```c
NSAllPredicateModifier
```

#### Discussion

The left hand side must be a collection. The corresponding predicate compares each value in the left hand side with the right hand side, and returns [`false`](../../../Swift/false.md) when it finds the first mismatch—or [`true`](../../../Swift/true.md) if all match.

## See Also

### Constants
- [NSComparisonPredicate.Modifier.direct](./direct.md)
  A predicate to compare directly the left and right hand sides.
- [NSComparisonPredicate.Modifier.any](./any.md)
  A predicate to match with any entry in the destination of a to-many relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/modifier/all)*