# init(_:)

**Framework**: Foundation Models  
**Kind**: init

Creates instructions from the content of a builder closure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(@InstructionsBuilder _ content: () throws -> Instructions) rethrows
```

## Parameters

- `content`: A closure that produces the instructions to give the model.

## See Also

- [struct InstructionsBuilder](instructionsbuilder.md)
  A type that represents an instructions builder.
- [protocol InstructionsRepresentable](instructionsrepresentable.md)
  A type that can be represented as instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructions/init(_:))*