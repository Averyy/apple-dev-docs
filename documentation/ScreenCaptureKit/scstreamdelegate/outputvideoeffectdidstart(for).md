# outputVideoEffectDidStart(for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that Presenter Overlay started.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func outputVideoEffectDidStart(for stream: SCStream)
```

```objc
- (void) outputVideoEffectDidStartForStream:(SCStream *) stream;
```

## Parameters

- `stream`: The stream using Presenter Overlay.

## See Also

### Responding to Presenter Overlay
- [func outputVideoEffectDidStop(for: SCStream)](./outputvideoeffectdidstop%28for%29.md)
  Tells the delegate that Presenter Overlay stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/outputvideoeffectdidstart(for:))*