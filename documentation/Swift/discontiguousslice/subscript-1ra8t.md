# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses a contiguous subrange of the collection’s elements.

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
subscript(bounds: Range<DiscontiguousSlice<Base>.Index>) -> DiscontiguousSlice<Base> { get }
```

#### Overview

For example, using a `PartialRangeFrom` range expression with an array accesses the subrange from the start of the range expression until the end of the array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2..<5]
print(streetsSlice)
// ["Channing", "Douglas", "Evarts"]
```

The accessed slice uses the same indices for the same elements as the original collection. This example searches `streetsSlice` for one of the strings in the slice, and then uses that index in the original array.

```swift
let index = streetsSlice.firstIndex(of: "Evarts")!    // 4
print(streets[index])
// "Evarts"
```

Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value. Attempting to access an element by using an index outside the bounds of the slice may result in a runtime error, even if that index is valid for the original collection.

```swift
print(streetsSlice.startIndex)
// 2
print(streetsSlice[2])
// "Channing"

print(streetsSlice[0])
// error: Index out of bounds
```

> **Note**: O(1)

## Parameters

- `bounds`: A range of the collection’s indices. The bounds of   the range must be valid indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/subscript(_:)-1ra8t)*