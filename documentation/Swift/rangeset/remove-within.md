# remove(_:within:)

**Framework**: Swift  
**Kind**: method

Removes the range that contains only the specified index from the range set.

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
mutating func remove<C>(_ index: Bound, within collection: C) where Bound == C.Index, C : Collection
```

#### Discussion

> **Note**: O(), where  is the number of ranges in the range set.

## Parameters

- `index`: The index to remove from the range set.   must be a   valid index of   that isn’t the collection’s  .
- `collection`: The collection that contains  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/remove(_:within:))*