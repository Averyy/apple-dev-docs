# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses a view of this collection with the elements at the given indices.

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
subscript(subranges: RangeSet<Self.Index>) -> DiscontiguousSlice<Self> { get }
```

#### Return Value

A collection of the elements at the positions in `subranges`.

#### Overview

> **Note**: O(1)

## Parameters

- `subranges`: The indices of the elements to retrieve from this   collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/subscript(_:)-4tv8v)*