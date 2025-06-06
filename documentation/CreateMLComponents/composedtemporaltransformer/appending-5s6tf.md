# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal transformer with a transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>> where Other : Transformer, Self.Output == Other.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer/appending(_:)-5s6tf)*