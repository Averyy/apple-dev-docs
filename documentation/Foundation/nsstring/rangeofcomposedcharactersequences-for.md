# rangeOfComposedCharacterSequences(for:)

**Framework**: Foundation  
**Kind**: method

Returns the range in the string of the composed character sequences for a given range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func rangeOfComposedCharacterSequences(for range: NSRange) -> NSRange
```

#### Return Value

The range in the receiver that includes the composed character sequences in `range`.

#### Discussion

This method provides a convenient way to grow a range to include all composed character sequences it overlaps.

## Parameters

- `range`: A range in the receiver. The range must not exceed the bounds of the receiver.

## See Also

- [func rangeOfComposedCharacterSequence(at: Int) -> NSRange](nsstring/rangeofcomposedcharactersequence(at:).md)
  Returns the range in the receiver of the composed character sequence located at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/rangeofcomposedcharactersequences(for:))*