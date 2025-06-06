# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal transformer with a transformer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>> where Other : Transformer, Other : Sendable, Self.Output == Other.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/appending(_:)-6v60w)*