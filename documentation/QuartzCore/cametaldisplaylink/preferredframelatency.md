# preferredFrameLatency

**Framework**: Core Animation  
**Kind**: property

The amount of time, in frames, your app requests to render a frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var preferredFrameLatency: Float { get set }
```

#### Discussion

The final latency may be bigger if the system needs more time, such as for windowed modes on macOS.

> ❗ **Important**:  The only acceptable values are `1.0` and `2.0`.

 The only acceptable values are `1.0` and `2.0`.

## See Also

- [var preferredFrameRateRange: CAFrameRateRange](cametaldisplaylink/preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var delegate: (any CAMetalDisplayLinkDelegate)?](cametaldisplaylink/delegate.md)
  An instance of a type your app implements that responds to the system’s callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/preferredframelatency)*