# +(_:_:)

**Framework**: Swift  
**Kind**: op

Creates a new collection by concatenating the elements of a sequence and a collection.

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
static func + <Other>(lhs: Other, rhs: Self) -> Self where Other : Sequence, Self.Element == Other.Element
```

#### Discussion

The two arguments must have the same `Element` type. For example, you can concatenate the elements of a `Range<Int>` instance and an integer array.

```swift
let numbers = [7, 8, 9, 10]
let moreNumbers = (1...6) + numbers
print(moreNumbers)
// Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

The resulting collection has the type of argument on the right-hand side. In the example above, `moreNumbers` has the same type as `numbers`, which is `[Int]`.

## Parameters

- `lhs`: A collection or finite sequence.
- `rhs`: A range-replaceable collection.

## See Also

- [func append<S>(contentsOf: S)](array/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](array/append(contentsof:)-9foli.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-n33n.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + (Array<Element>, Array<Element>) -> Array<Element>](array/+(_:_:).md)
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-9fm5l.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](array/+=(_:_:)-676ib.md)
  Appends the elements of a sequence to a range-replaceable collection.
- [static func += (inout Array<Element>, Array<Element>)](array/+=(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/+(_:_:)-6h58k)*