# CTFrameGetFrameAttributes(_:)

**Framework**: Core Text  
**Kind**: func

Returns the frame attributes used to create the frame.

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
func CTFrameGetFrameAttributes(_ frame: CTFrame) -> CFDictionary?
```

#### Return Value

A reference to a CFDictionary object containing the frame attributes that were used to create the frame, or, if the frame was created without any frame attributes, `NULL`.

#### Discussion

You can create a frame with an attributes dictionary to control various aspects of the framing process. These attributes are different from the ones used to create an attributed string.

## Parameters

- `frame`: The frame whose attributes are returned.

## See Also

- [func CTFrameGetStringRange(CTFrame) -> CFRange](ctframegetstringrange(_:).md)
  Returns the range of characters originally requested to fill the frame.
- [func CTFrameGetVisibleStringRange(CTFrame) -> CFRange](ctframegetvisiblestringrange(_:).md)
  Returns the range of characters that actually fit in the frame.
- [func CTFrameGetPath(CTFrame) -> CGPath](ctframegetpath(_:).md)
  Returns the path used to create the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframegetframeattributes(_:))*