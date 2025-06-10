# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Accesses a contiguous subrange of the collection’s elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(bounds: Range<Self.Index>) -> Slice<Self> { get }
```

#### Overview

The accessed slice uses the same indices for the same elements as the original collection. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```None
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let index = streetsSlice.firstIndex(of: "Evarts")    // 4
print(streets[index!])
// Prints "Evarts"
```

> **Note**: O(1)

## Parameters

- `bounds`: A range of the collection’s indices. The bounds of   the range must be valid indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/subscript(_:)-79vvr)*