# joined(separator:)

**Framework**: SwiftData  
**Kind**: method

Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func joined<Separator>(separator: Separator) -> JoinedSequence<Self> where Separator : Sequence, Separator.Element == Self.Element.Element
```

#### Return Value

The joined sequence of elements.

#### Discussion

This example shows how an array of `[Int]` instances can be joined, using another `[Int]` instance as the separator:

```swift
let nestedNumbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let joined = nestedNumbers.joined(separator: [-1, -2])
print(Array(joined))
// Prints "[1, 2, 3, -1, -2, 4, 5, 6, -1, -2, 7, 8, 9]"
```

## Parameters

- `separator`: A sequence to insert between each of this   sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchresultscollection/joined(separator:)-8ubfx)*