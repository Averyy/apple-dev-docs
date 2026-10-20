# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Scales an input.

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
func applied(to input: Element, eventHandler: EventHandler? = nil) -> Element
```

**Other overloads**:

```swift
func applied<S>(to input: S, eventHandler: EventHandler? = nil) -> [Element] where Element == S.Element, S : Sequence
```

#### Return Value

A scaled value.

## Parameters

- `input`: A floating-point value.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartransformer/applied(to:eventhandler:))*