# untilFinished(_:)

**Framework**: Observation  
**Kind**: method

Constructs an asynchronous sequence for a given closure by tracking changes of `@Observable` types.

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
static func untilFinished(_ emit: @escaping @isolated(any) () throws(Failure) -> Observations<Element, Failure>.Iteration) -> Observations<Element, Failure>
```

#### Discussion

The emit closure is responsible for extracting a value out of a single or many `@Observable` types. This method continues to be invoked until the .finished option is returned or an error is thrown.

## Parameters

- `emit`: A closure to generate an element for the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observations/untilfinished(_:))*