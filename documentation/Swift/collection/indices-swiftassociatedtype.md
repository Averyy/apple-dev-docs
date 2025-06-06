# Indices

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

A type that represents the indices that are valid for subscripting the collection, in ascending order.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
associatedtype Indices : Collection = DefaultIndices<Self> where Self.Indices == Self.Indices.SubSequence
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/indices-swift.associatedtype)*