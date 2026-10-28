# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript

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

## Overview

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

- `bounds`: A range of integers. The bounds of the range must be valid indices of the array.

## See Also

### Accessing Elements
- [subscript(Int) -> Element](./subscript%28_%29-25iat.md)
  Accesses the element at the specified position.
- [var first: Self.Element?](./first.md)
  The first element of the collection.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-3pmfg.md)
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/subscript(_:)-53fvb)*