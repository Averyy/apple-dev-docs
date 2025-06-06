# applied(to:generator:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Performs the random transformation on a single input.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func applied(to input: Self.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> Self.Output
```

#### Return Value

An output produced by applying the random transformer to the input.

## Parameters

- `input`: The random transformer input.
- `generator`: A random number generator.
- `eventHandler`: An event handler.

## See Also

- [associatedtype Input](randomtransformer/input.md)
  The input type.
- [associatedtype Output](randomtransformer/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomtransformer/applied(to:generator:eventhandler:))*