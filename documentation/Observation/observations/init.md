# init(_:)

**Framework**: Observation  
**Kind**: init

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
init(_ emit: @escaping @isolated(any) () throws(Failure) -> Element)
```

#### Discussion

The emit closure is responsible for extracting a value out of a single or many `@Observable` types.

## Parameters

- `emit`: A closure to generate an element for the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observations/init(_:))*