# +(_:_:)

**Framework**: Swift  
**Kind**: op

Creates a new collection by concatenating the elements of two collections.

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
static func + <Other>(lhs: Self, rhs: Other) -> Self where Other : RangeReplaceableCollection, Self.Element == Other.Element
```

#### Discussion

The two arguments must have the same `Element` type. For example, you can concatenate the elements of two integer arrays.

```swift
let lowerNumbers = [1, 2, 3, 4]
let higherNumbers: ContiguousArray = [5, 6, 7, 8, 9, 10]
let allNumbers = lowerNumbers + higherNumbers
print(allNumbers)
// Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

The resulting collection has the type of the argument on the left-hand side. In the example above, `moreNumbers` has the same type as `numbers`, which is `[Int]`.

## Parameters

- `lhs`: A range-replaceable collection.
- `rhs`: Another range-replaceable collection.

## See Also

- [func append(String)](string/append(_:)-4xa8f.md)
  Appends the given string to this string.
- [func append(Character)](string/append(_:)-4xi3j.md)
  Appends the given character to the string.
- [func append(contentsOf: String)](string/append(contentsof:)-oxek.md)
- [func append(contentsOf: Substring)](string/append(contentsof:)-9vb4t.md)
- [func append<S>(contentsOf: S)](string/append(contentsof:)-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](string/append(contentsof:)-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func reserveCapacity(Int)](string/reservecapacity(_:).md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [static func + (String, String) -> String](string/+(_:_:).md)
- [static func += (inout String, String)](string/+=(_:_:).md)
- [static func + <Other>(Other, Self) -> Self](string/+(_:_:)-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](string/+(_:_:)-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](string/+=(_:_:)-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/+(_:_:)-9fm57)*