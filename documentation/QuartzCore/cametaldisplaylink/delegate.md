# delegate

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, nullable) id<CAMetalDisplayLinkDelegate> delegate;
```

## See Also

### Configuring a Display Link
- [var preferredFrameRateRange: CAFrameRateRange](./preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFrameLatency: Float](./preferredframelatency.md)
  The amount of time, in frames, your app requests to render a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/delegate)*