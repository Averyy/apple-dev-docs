# CTFrameGetVisibleStringRange(_:)

**Framework**: Core Text  
**Kind**: func

Returns the range of characters that actually fit in the frame.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFrameGetVisibleStringRange(_ frame: CTFrame) -> CFRange
```

#### Return Value

A `CFRange` structure containing the backing store range of characters that fit into the frame, or if the function call is not successful or no characters fit in the frame, an empty range.

#### Discussion

This function can be used to cascade frames, because it returns the range of characters that can be seen in the frame. The next frame would start where this frame ends.

## Parameters

- `frame`: The frame whose visible character range is returned.

## See Also

- [func CTFrameGetStringRange(CTFrame) -> CFRange](ctframegetstringrange(_:).md)
  Returns the range of characters originally requested to fill the frame.
- [func CTFrameGetPath(CTFrame) -> CGPath](ctframegetpath(_:).md)
  Returns the path used to create the frame.
- [func CTFrameGetFrameAttributes(CTFrame) -> CFDictionary?](ctframegetframeattributes(_:).md)
  Returns the frame attributes used to create the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframegetvisiblestringrange(_:))*