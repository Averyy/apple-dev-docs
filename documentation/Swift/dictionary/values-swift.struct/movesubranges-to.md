# moveSubranges(_:to:)

**Framework**: Swift  
**Kind**: method

Moves the elements in the given subranges to just before the element at the specified index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@discardableResult
mutating func moveSubranges(_ subranges: RangeSet<Self.Index>, to insertionPoint: Self.Index) -> Range<Self.Index>
```

#### Return Value

The new bounds of the moved elements.

#### Discussion

This example finds all the uppercase letters in the array and then moves them to between `"i"` and `"j"`.

```swift
var letters = Array("ABCdeFGhijkLMNOp")
let uppercaseRanges = letters.indices(where: { $0.isUppercase })
let rangeOfUppercase = letters.moveSubranges(uppercaseRanges, to: 10)
// String(letters) == "dehiABCFGLMNOjkp"
// rangeOfUppercase == 4..<13
```

> **Note**: O( log ) where  is the length of the collection.

## Parameters

- `subranges`: The subranges of the elements to move.
- `insertionPoint`: The index to use as the destination of the elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/movesubranges(_:to:))*