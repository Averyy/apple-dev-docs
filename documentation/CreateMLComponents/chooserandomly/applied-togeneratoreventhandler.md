# applied(to:generator:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Chooses a random transformer from a list of transformers and applies the chosen transformer.

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
func applied(to input: Element, generator: inout some RandomNumberGenerator, eventHandler: EventHandler? = nil) async throws -> Element
```

#### Return Value

The augmented input.

## Parameters

- `input`: The input to the transformer.
- `generator`: A random number generator.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/chooserandomly/applied(to:generator:eventhandler:))*