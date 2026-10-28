# stop()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Forces the external display configurator to asynchronously stop configuring the external display.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

## Discussion

Call [`stop()`](./stop%28%29.md) to force the [`AVCaptureExternalDisplayConfigurator`](../avcaptureexternaldisplayconfigurator.md) to asynchronously stop configuring the external display. Once stopped, the [`isActive`](./isactive.md) property changes to `false` and the [`activeExternalDisplayFrameRate`](./activeexternaldisplayframerate.md) becomes 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/stop())*