# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Accesses the element at the specified position.

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
subscript(position: Self.Index) -> Self.Element { get }
```

#### Overview

The following example accesses an element of an array through its subscript to print its value:

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
print(streets[1])
// Prints "Bryant"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> **Complexity**: O(1)

## Parameters

- `position`: The position of the element to access. `position` must be a valid index of the collection that is not equal to the `endIndex` property.

## Default Implementations

### Collection Implementations
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-2ew5d.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-593m9.md)
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./subscript%28_%29-6dbv1.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-6nizk.md)
  Accesses a contiguous subrange of the collection’s elements.
### MutableCollection Implementations
- [subscript<R>(R) -> Self.SubSequence](../mutablecollection/subscript%28_%29-1wd4v.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](../mutablecollection/subscript%28_%29-2qem1.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(UnboundedRange) -> Self.SubSequence](../mutablecollection/subscript%28_%29-37d4d.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/subscript(_:)-887tm)*