# SNTimeDurationConstraint.enumeratedDurations(_:)

**Framework**: Sound Analysis  
**Kind**: case

A constraint that defines acceptable time window durations in a discrete list.

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
case enumeratedDurations([CMTime])
```

## Parameters

- `timeDurations`: An array of time durations the request’s underlying sound classifier accepts.

## See Also

- [SNTimeDurationConstraint.durationRange(_:)](sntimedurationconstraint-swift.enum/durationrange(_:).md)
  A constraint that defines acceptable time window durations with a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/sntimedurationconstraint-swift.enum/enumerateddurations(_:))*