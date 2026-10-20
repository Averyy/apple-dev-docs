# outputVideoEffectDidStop(for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that Presenter Overlay stopped.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func outputVideoEffectDidStop(for stream: SCStream)
```

```objc
- (void) outputVideoEffectDidStopForStream:(SCStream *) stream;
```

## Parameters

- `stream`: The stream that was using Presenter Overlay.

## See Also

### Responding to Presenter Overlay
- [func outputVideoEffectDidStart(for: SCStream)](./outputvideoeffectdidstart%28for%29.md)
  Tells the delegate that Presenter Overlay started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/outputvideoeffectdidstop(for:))*