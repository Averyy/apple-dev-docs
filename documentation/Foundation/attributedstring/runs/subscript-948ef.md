# subscript(_:_:_:)

**Framework**: Foundation  
**Kind**: subscript

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
subscript<T, U, V>(t: T.Type, u: U.Type, v: V.Type) -> AttributedString.Runs.AttributesSlice3<T, U, V> where T : AttributedStringKey, U : AttributedStringKey, V : AttributedStringKey, T.Value : Sendable, U.Value : Sendable, V.Value : Sendable { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs/subscript(_:_:_:)-948ef)*