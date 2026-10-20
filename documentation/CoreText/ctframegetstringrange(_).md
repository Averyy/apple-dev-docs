# CTFrameGetStringRange(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the range of characters originally requested to fill the frame.

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
func CTFrameGetStringRange(_ frame: CTFrame) -> CFRange
```

```c
extern CFRange CTFrameGetStringRange(CTFrameRef frame);
```

#### Return Value

A `CFRange` structure containing the backing store range of characters that were originally requested to fill the frame, or, if the function call is not successful, an empty range.

## Parameters

- `frame`: The frame whose character range is returned.

## See Also

### Getting Frame Data
- [func CTFrameGetVisibleStringRange(CTFrame) -> CFRange](./ctframegetvisiblestringrange%28_%29.md)
  Returns the range of characters that actually fit in the frame.
- [func CTFrameGetPath(CTFrame) -> CGPath](./ctframegetpath%28_%29.md)
  Returns the path used to create the frame.
- [func CTFrameGetFrameAttributes(CTFrame) -> CFDictionary?](./ctframegetframeattributes%28_%29.md)
  Returns the frame attributes used to create the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframegetstringrange(_:))*