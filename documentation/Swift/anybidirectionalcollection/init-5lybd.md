# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a type-erased collection that wraps the given collection.

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
init<C>(_ base: C) where Element == C.Element, C : BidirectionalCollection
```

#### Discussion

> **Note**: O(1).

O(1).

## Parameters

- `base`: The collection to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection/init(_:)-5lybd)*