# subscript(_:_:_:_:_:)

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
subscript<T, U, V, W, X>(t: KeyPath<AttributeDynamicLookup, T>, u: KeyPath<AttributeDynamicLookup, U>, v: KeyPath<AttributeDynamicLookup, V>, w: KeyPath<AttributeDynamicLookup, W>, x: KeyPath<AttributeDynamicLookup, X>) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X> where T : AttributedStringKey, U : AttributedStringKey, V : AttributedStringKey, W : AttributedStringKey, X : AttributedStringKey, T.Value : Sendable, U.Value : Sendable, V.Value : Sendable, W.Value : Sendable, X.Value : Sendable { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs/subscript(_:_:_:_:_:)-9i87e)*