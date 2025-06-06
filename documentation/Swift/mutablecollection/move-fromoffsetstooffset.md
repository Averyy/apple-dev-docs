# move(fromOffsets:toOffset:)

**Framework**: Swift  
**Kind**: method

Moves all the elements at the specified offsets to the specified destination offset, preserving ordering.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func move(fromOffsets source: IndexSet, toOffset destination: Int)
```

#### Discussion

Pass an offset as `destination` to indicate where in the collection the moved elements should be inserted. Of the elements that are not represented by the offsets in `source`, those before `destination` are moved toward the beginning of the collection to make room for the moved elements, while those at or after `destination` are moved toward the end.

In this example, demonstrating moving several elements to different destination offsets, `lowercaseOffsets` represents the offsets of the lowercase elements in `letters`:

```swift
var letters = Array("ABcDefgHIJKlmNO")
let lowercaseOffsets = IndexSet(...)
letters.move(fromOffsets: lowercaseOffsets, toOffset: 2)
// String(letters) == "ABcefglmDHIJKNO"

// Reset the `letters` array.
letters = Array("ABcDefgHIJKlmNO")
letters.move(fromOffsets: lowercaseOffsets, toOffset: 15)
// String(letters) == "ABDHIJKNOcefglm"
```

If `source` represents a single element, calling this method with its own offset, or the offset of the following element, as `destination` has no effect.

```swift
letters = Array("ABcDefgHIJKlmNO")
letters.move(fromOffsets: IndexSet(integer: 2), toOffset: 2)
// String(letters) == "ABcDefgHIJKlmNO"
```

> **Note**: O( log ), where  is the length of the collection.

O( log ), where  is the length of the collection.

## Parameters

- `source`: An index set representing the offsets of all elements that   should be moved.
- `destination`: The offset of the element before which to insert the   moved elements.   must be in the closed range   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablecollection/move(fromoffsets:tooffset:))*