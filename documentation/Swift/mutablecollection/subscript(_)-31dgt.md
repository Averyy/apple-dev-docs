# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Accesses a contiguous subrange of the collection’s elements.

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
override subscript(bounds: Range<Self.Index>) -> Self.SubSequence { get set }
```

## Overview

The accessed slice uses the same indices for the same elements as the original collection. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let index = streetsSlice.firstIndex(of: "Evarts")    // 4
streets[index!] = "Eustace"
print(streets[index!])
// Prints "Eustace"
```

> **Complexity**: O(1)

## Parameters

- `bounds`: A range of the collection’s indices. The bounds of the range must be valid indices of the collection.

## Default Implementations

### MutableCollection Implementations
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-1wd4v.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-2qem1.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-37d4d.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablecollection/subscript(_:)-31dgt)*