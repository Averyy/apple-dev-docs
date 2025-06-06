# append(contentsOf:)

**Framework**: Swift  
**Kind**: method

Adds the elements of a sequence to the end of the array.

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
mutating func append<S>(contentsOf newElements: S) where Element == S.Element, S : Sequence
```

#### Discussion

Use this method to append the elements of a sequence to the end of this array. This example appends the elements of a `Range<Int>` instance to an array of integers.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(contentsOf: 10...15)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]"
```

> **Note**: O() on average, where  is the length of `newElements`, over many calls to `append(contentsOf:)` on the same array.

## Parameters

- `newElements`: The elements to append to the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/append(contentsof:))*