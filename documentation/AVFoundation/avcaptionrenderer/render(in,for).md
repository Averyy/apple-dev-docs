# render(in:for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Draw the captions for the time you specify.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func render(in ctx: CGContext, for time: CMTime)
```

```objc
- (void) renderInContext:(CGContextRef) ctx forTime:(CMTime) time;
```

## Parameters

- `ctx`: The drawing content.
- `time`: The time value for which the system draws the captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/render(in:for:))*