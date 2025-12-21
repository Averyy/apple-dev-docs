# stop()

**Framework**: AVFoundation  
**Kind**: method

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

#### Discussion

Call [`stop()`](avcaptureexternaldisplayconfigurator/stop().md) to force the [`AVCaptureExternalDisplayConfigurator`](avcaptureexternaldisplayconfigurator.md) to asynchronously stop configuring the external display. Once stopped, the [`isActive`](avcaptureexternaldisplayconfigurator/isactive.md) property changes to `false` and the [`activeExternalDisplayFrameRate`](avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.md) becomes 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/stop())*