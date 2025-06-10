# lexicographicallyPrecedes(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.

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
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

#### Return Value

`true` if this sequence precedes `other` in a dictionary ordering; otherwise, `false`.

#### Discussion

This example uses the `lexicographicallyPrecedes` method to test which array of integers comes first in a lexicographical ordering.

```swift
let a = [1, 2, 2, 2]
let b = [1, 2, 3, 4]

print(a.lexicographicallyPrecedes(b))
// Prints "true"
print(b.lexicographicallyPrecedes(b))
// Prints "false"
```

> **Note**: This method implements the mathematical notion of lexicographical ordering, which has no connection to Unicode.  If you are sorting strings to present to the end user, use `String` APIs that perform localized comparison.

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `other`.

## Parameters

- `other`: A sequence to compare to this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/words-swift.struct/lexicographicallyprecedes(_:))*