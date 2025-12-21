# Observations

**Framework**: Observation  
**Kind**: struct

An asychronous sequence generated from a closure that tracks the transactional changes of `@Observable` types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Observations<Element, Failure> where Element : Sendable, Failure : Error
```

#### Overview

`Observations` conforms to `AsyncSequence`, providing a intutive and safe mechanism to track changes to types that are marked as `@Observable` by using Swift Concurrency to indicate transactional boundaries starting from the willSet of the first mutation to the next suspension point of the safe access.

## Topics

### Structures
- [Observations.Iterator](observations/iterator.md)
### Initializers
- [init(() throws(Failure) -> Element)](observations/init(_:).md)
  Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.
### Type Methods
- [static func untilFinished(() throws(Failure) -> Observations<Element, Failure>.Iteration) -> Observations<Element, Failure>](observations/untilfinished(_:).md)
  Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.
### Enumerations
- [Observations.Iteration](observations/iteration.md)

## Relationships

### Conforms To
- [AsyncSequence](../swift/asyncsequence.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observations)*