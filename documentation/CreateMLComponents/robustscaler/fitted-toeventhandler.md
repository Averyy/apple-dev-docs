# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a robust scaler to a sequence of elements.

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
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) throws -> RobustScaler<Element>.Transformer where Element == S.Element, S : Sequence
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of elements.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler/fitted(to:eventhandler:))*