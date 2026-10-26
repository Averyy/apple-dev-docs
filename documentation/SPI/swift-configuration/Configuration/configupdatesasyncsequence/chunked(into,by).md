---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(into:by:)"
framework: "swift-configuration/Configuration"
---

# chunked(into:by:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(into:by:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Collected>(into: Collected.Type, by belongInSameGroup: @escaping @Sendable (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(into:by:))*