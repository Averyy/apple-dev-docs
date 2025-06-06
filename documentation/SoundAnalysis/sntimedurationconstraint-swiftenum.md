# SNTimeDurationConstraint

**Framework**: Sound Analysis  
**Kind**: enum

Defines the time duration windows the request’s underlying sound classifier accepts with a range, or an array, of durations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum SNTimeDurationConstraint
```

## Topics

### Inspecting a Constraint
- [SNTimeDurationConstraint.durationRange(_:)](sntimedurationconstraint-swift.enum/durationrange(_:).md)
  A constraint that defines acceptable time window durations with a range.
- [SNTimeDurationConstraint.enumeratedDurations(_:)](sntimedurationconstraint-swift.enum/enumerateddurations(_:).md)
  A constraint that defines acceptable time window durations in a discrete list.

## See Also

- [var knownClassifications: [String]](snclassifysoundrequest/knownclassifications.md)
  A string array that contains every prediction label in the request’s underlying sound classifier model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/sntimedurationconstraint-swift.enum)*