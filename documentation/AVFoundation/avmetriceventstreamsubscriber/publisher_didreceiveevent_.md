# publisher:didReceiveEvent:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the subscriber that the publisher produced a metric event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
- (void) publisher:(id<AVMetricEventStreamPublisher>) publisher didReceiveEvent:(AVMetricEvent *) event;
```

## Parameters

- `publisher`: The publisher.
- `event`: The metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetriceventstreamsubscriber/publisher:didreceiveevent:)*