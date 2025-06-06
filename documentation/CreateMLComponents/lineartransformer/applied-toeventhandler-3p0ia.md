# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Scales a sequence of inputs.

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
func applied<S>(to input: S, eventHandler: EventHandler? = nil) -> [Element] where Element == S.Element, S : Sequence
```

#### Return Value

An array of scaled values.

## Parameters

- `input`: A sequence of input values.
- `eventHandler`: An event handler.

## See Also

- [func applied(to: Element, eventHandler: EventHandler?) -> Element](lineartransformer/applied(to:eventhandler:)-6w4yg.md)
  Scales an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartransformer/applied(to:eventhandler:)-3p0ia)*