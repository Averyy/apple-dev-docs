# subscript(_:)

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
subscript<T>(keyPath: KeyPath<AttributeDynamicLookup, T>) -> AttributedString.Runs.AttributesSlice1<T> where T : AttributedStringKey, T.Value : Sendable { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs/subscript(_:)-6aptr)*