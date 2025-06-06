# insert(_:within:)

**Framework**: Swift  
**Kind**: method

Inserts a range that contains only the specified index into the range set.

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
@discardableResult
mutating func insert<C>(_ index: Bound, within collection: C) -> Bool where Bound == C.Index, C : Collection
```

#### Return Value

`true` if the range set was modified, or `false` if the given `index` was already in the range set.

#### Discussion

> **Note**: O(), where  is the number of ranges in the range set.

## Parameters

- `index`: The index to insert into the range set.   must be a   valid index of   that isn’t the collection’s  .
- `collection`: The collection that contains  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/insert(_:within:))*