# append(contentsOf:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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

## Discussion

Use this method to append the elements of a sequence to the end of this array. This example appends the elements of a `Range<Int>` instance to an array of integers.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(contentsOf: 10...15)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]"
```

> **Complexity**: O(*m*) on average, where *m* is the length of `newElements`, over many calls to `append(contentsOf:)` on the same array.

## Parameters

- `newElements`: The elements to append to the array.

## See Also

### Combining Arrays
- [func append<S>(contentsOf: S)](./append%28contentsof%29-9foli.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [static func + <Other>(Other, Self) -> Self](./plus%28_,_%29-6h58k.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-n33n.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + (Array<Element>, Array<Element>) -> Array<Element>](./plus%28_,_%29.md)
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-9fm5l.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](./pluseq%28_,_%29-676ib.md)
  Appends the elements of a sequence to a range-replaceable collection.
- [static func += (inout Array<Element>, Array<Element>)](./pluseq%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/append(contentsof:))*