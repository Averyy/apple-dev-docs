# CTFrameGetPath(_:)

**Framework**: Core Text  
**Kind**: func

Returns the path used to create the frame.

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
func CTFrameGetPath(_ frame: CTFrame) -> CGPath
```

## Parameters

- `frame`: The frame whose path is returned.

## See Also

- [func CTFrameGetStringRange(CTFrame) -> CFRange](ctframegetstringrange(_:).md)
  Returns the range of characters originally requested to fill the frame.
- [func CTFrameGetVisibleStringRange(CTFrame) -> CFRange](ctframegetvisiblestringrange(_:).md)
  Returns the range of characters that actually fit in the frame.
- [func CTFrameGetFrameAttributes(CTFrame) -> CFDictionary?](ctframegetframeattributes(_:).md)
  Returns the frame attributes used to create the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframegetpath(_:))*