# rangeOfComposedCharacterSequence(at:)

**Framework**: Foundation  
**Kind**: method

Returns the range in the receiver of the composed character sequence located at a given index.

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
func rangeOfComposedCharacterSequence(at index: Int) -> NSRange
```

#### Return Value

The range in the receiver of the composed character sequence located at `anIndex`.

#### Discussion

The composed character sequence includes the first decomposed base letter found at or before `anIndex`, and its length includes the decomposed base letter and all combining characters that follow.

## Parameters

- `index`: The index of a character in the receiver. The value must not exceed the bounds of the receiver.

## See Also

- [func rangeOfComposedCharacterSequences(for: NSRange) -> NSRange](nsstring/rangeofcomposedcharactersequences(for:).md)
  Returns the range in the string of the composed character sequences for a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/rangeofcomposedcharactersequence(at:))*