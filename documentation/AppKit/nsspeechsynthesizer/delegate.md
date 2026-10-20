# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The synthesizer’s delegate.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
weak var delegate: (any NSSpeechSynthesizerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSpeechSynthesizerDelegate> delegate;
```

## See Also

### Customizing the Speech Synthesizer Behavior
- [protocol NSSpeechSynthesizerDelegate](../nsspeechsynthesizerdelegate.md)
  A set of optional methods implemented by delegates of [`NSSpeechSynthesizer`](../nsspeechsynthesizer.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/delegate)*