# +=(_:_:)

**Framework**: Swift  
**Kind**: op

Appends the elements of a sequence to a range-replaceable collection.

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
static func += <Other>(lhs: inout Self, rhs: Other) where Other : Sequence, Self.Element == Other.Element
```

#### Discussion

Use this operator to append the elements of a sequence to the end of range-replaceable collection with same `Element` type. This example appends the elements of a `Range<Int>` instance to an array of integers.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers += 10...15
print(numbers)
// Prints "[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]"
```

> **Note**: O(), where  is the length of the right-hand-side argument.

## Parameters

- `lhs`: The array to append to.
- `rhs`: A collection or finite sequence.

## See Also

- [func append<S>(contentsOf: S)](array/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](array/append(contentsof:)-9foli.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [static func + <Other>(Other, Self) -> Self](array/+(_:_:)-6h58k.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-n33n.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + (Array<Element>, Array<Element>) -> Array<Element>](array/+(_:_:).md)
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-9fm5l.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += (inout Array<Element>, Array<Element>)](array/+=(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/+=(_:_:)-676ib)*