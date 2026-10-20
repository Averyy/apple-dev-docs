# +(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

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

### Appending Strings and Characters
- [func append(String)](./append%28_%29-4xa8f.md)
  Appends the given string to this string.
- [func append(Character)](./append%28_%29-4xi3j.md)
  Appends the given character to the string.
- [func append(contentsOf: String)](./append%28contentsof%29-oxek.md)
- [func append(contentsOf: Substring)](./append%28contentsof%29-9vb4t.md)
- [func append<S>(contentsOf: S)](./append%28contentsof%29-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](./append%28contentsof%29-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [static func + (String, String) -> String](./plus%28_,_%29.md)
- [static func += (inout String, String)](./pluseq%28_,_%29.md)
- [static func + <Other>(Other, Self) -> Self](./plus%28_,_%29-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](./pluseq%28_,_%29-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/+(_:_:)-9fm57)*