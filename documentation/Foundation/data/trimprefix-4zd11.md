# trimPrefix(_:)

**Framework**: Foundation  
**Kind**: method

Removes `prefix` from the start of the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func trimPrefix<Prefix>(_ prefix: Prefix) where Prefix : Sequence, Self.Element == Prefix.Element
```

## Parameters

- `prefix`: The collection to remove from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/trimprefix(_:)-4zd11)*