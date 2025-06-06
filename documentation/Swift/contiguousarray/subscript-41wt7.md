# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses a contiguous subrange of the array’s elements.

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
subscript(bounds: Range<Int>) -> ArraySlice<Element> { get set }
```

#### Overview

The returned `ArraySlice` instance uses the same indices for the same elements as the original array. In particular, that slice, unlike an array, may have a nonzero `startIndex` and an `endIndex` that is not equal to `count`. Always use the slice’s `startIndex` and `endIndex` properties instead of assuming that its indices start or end at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let i = streetsSlice.firstIndex(of: "Evarts")    // 4
print(streets[i!])
// Prints "Evarts"
```

## Parameters

- `bounds`: A range of integers. The bounds of the range must be   valid indices of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/subscript(_:)-41wt7)*