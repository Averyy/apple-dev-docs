# applied(to:generator:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the random apply operation on the input.

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
final func applied(to input: RandomTransformer.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler? = nil) async throws -> RandomTransformer.Output
```

#### Return Value

The randomly transformed image.

## Parameters

- `input`: An input.
- `generator`: A random number generator.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/uniformrandomintegerparameter/applied(to:generator:eventhandler:))*