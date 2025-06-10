# +=(_:_:)

**Framework**: MusicKit  
**Kind**: op

Appends the elements of a sequence to a range-replaceable collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/+=(_:_:))*