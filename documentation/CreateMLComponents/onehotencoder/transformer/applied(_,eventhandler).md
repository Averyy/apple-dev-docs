# applied(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a one-hot encoding on a sequence of inputs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func applied<S>(_ input: S, eventHandler: EventHandler? = nil) throws -> [[Int]] where S : Sequence, S.Element == Category?
```

#### Return Value

An array of one-hot encoded arrays.

## Parameters

- `input`: A sequence of input values.
- `eventHandler`: An event handler.

## See Also

- [func applied(to: Category?, eventHandler: EventHandler?) throws -> [Int]](onehotencoder/transformer/applied(to:eventhandler:).md)
  Performs a one-hot encoding on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/transformer/applied(_:eventhandler:))*