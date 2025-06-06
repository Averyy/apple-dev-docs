# backgroundColor(at:)

**Framework**: AVFoundation  
**Kind**: method

Returns the background color at the index position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func backgroundColor(at index: String.Index) -> (CGColor?, Range<String.Index>)
```

#### Return Value

A tuple that contains the background color and range to which it applies.

## Parameters

- `index`: A character position in the caption text.

## See Also

- [func textColor(at: String.Index) -> (CGColor?, Range<String.Index>)](avcaption/textcolor(at:).md)
  Returns the text color at the index position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/backgroundcolor(at:))*