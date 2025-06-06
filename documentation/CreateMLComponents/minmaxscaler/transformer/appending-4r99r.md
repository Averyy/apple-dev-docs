# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with a temporal transformer.

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
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other> where Self : Sendable, Other : TemporalTransformer, Self.Output == Other.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/transformer/appending(_:)-4r99r)*