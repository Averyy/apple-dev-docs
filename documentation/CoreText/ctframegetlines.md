# CTFrameGetLines(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of lines stored in the frame.

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
func CTFrameGetLines(_ frame: CTFrame) -> CFArray
```

#### Return Value

A CFArray object containing the CTLine objects that make up the frame, or, if there are no lines in the frame, an array with no elements.

## Parameters

- `frame`: The frame whose line array is returned.

## See Also

- [func CTFrameGetLineOrigins(CTFrame, CFRange, UnsafeMutablePointer<CGPoint>)](ctframegetlineorigins(_:_:_:).md)
  Copies a range of line origins for a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframegetlines(_:))*