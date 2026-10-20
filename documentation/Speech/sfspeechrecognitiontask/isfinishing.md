# isFinishing

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether audio input has stopped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var isFinishing: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFinishing) BOOL finishing;
```

#### Discussion

By default, the value of this property is `false`.

## See Also

### Finishing a speech recognition task
- [func finish()](./finish%28%29.md)
  Stops accepting new audio and finishes processing on the audio input that has already been accepted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/isfinishing)*