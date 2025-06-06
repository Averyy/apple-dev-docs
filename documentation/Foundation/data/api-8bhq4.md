# +(_:_:)

**Framework**: Foundation  
**Kind**: op

Creates a new collection by concatenating the elements of a sequence and a collection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func + <Other>(lhs: Other, rhs: Self) -> Self where Other : Sequence, Self.Element == Other.Element
```

#### Discussion

The two arguments must have the same `Element` type. For example, you can concatenate the elements of a `Range<Int>` instance and an integer array.

```None
let numbers = [7, 8, 9, 10]
let moreNumbers = (1...6) + numbers
print(moreNumbers)
// Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

The resulting collection has the type of argument on the right-hand side. In the example above, `moreNumbers` has the same type as `numbers`, which is `[Int]`.

## Parameters

- `lhs`: A collection or finite sequence.
- `rhs`: A range-replaceable collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/+(_:_:)-8bhq4)*