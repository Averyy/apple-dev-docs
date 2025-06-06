# subscript(_:_:)

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
subscript<T, U>(t: T.Type, u: U.Type) -> AttributedString.Runs.AttributesSlice2<T, U> where T : AttributedStringKey, U : AttributedStringKey, T.Value : Sendable, U.Value : Sendable { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs/subscript(_:_:)-3taux)*