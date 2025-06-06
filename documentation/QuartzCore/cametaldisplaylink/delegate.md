# delegate

**Framework**: Core Animation  
**Kind**: property

An instance of a type your app implements that responds to the system’s callbacks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any CAMetalDisplayLinkDelegate)? { get set }
```

## See Also

- [var preferredFrameRateRange: CAFrameRateRange](cametaldisplaylink/preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFrameLatency: Float](cametaldisplaylink/preferredframelatency.md)
  The amount of time, in frames, your app requests to render a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/delegate)*