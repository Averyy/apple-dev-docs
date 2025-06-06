# applied(to:generator:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Randomly applies a transformer on an input.

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
func applied(to input: RandomTransformer.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler? = nil) async throws -> RandomTransformer.Output
```

#### Return Value

The randomly transformed input.

## Parameters

- `input`: The input.
- `generator`: A random number generator.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/applyrandomly/applied(to:generator:eventhandler:))*