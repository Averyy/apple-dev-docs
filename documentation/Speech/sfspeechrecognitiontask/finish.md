# finish()

**Framework**: Speech  
**Kind**: method

Stops accepting new audio and finishes processing on the audio input that has already been accepted.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func finish()
```

#### Discussion

For audio buffer–based recognition, recognition does not finish until this method is called, so be sure to call it when the audio source is exhausted.

## See Also

- [var isFinishing: Bool](sfspeechrecognitiontask/isfinishing.md)
  A Boolean value that indicates whether audio input has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/finish())*