# +(_:_:)

**Framework**: MusicKit  
**Kind**: op

Creates a new collection by concatenating the elements of two collections.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/+(_:_:)-xw4q)*