# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with a temporal transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other> where Other : TemporalTransformer, Self.Output == Other.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imputetransformer/appending(_:)-4rj53)*