# CTFrameDraw(_:_:)

**Framework**: Core Text  
**Kind**: func

Draws an entire frame into a context.

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
func CTFrameDraw(_ frame: CTFrame, _ context: CGContext)
```

#### Discussion

If both the frame and the context are valid, the frame is drawn in the context. This call can leave the context in any state and does not flush it after the draw operation.

## Parameters

- `frame`: The frame to draw.
- `context`: The context in which to draw the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframedraw(_:_:))*