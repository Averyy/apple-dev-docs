# requiresOnDeviceRecognition

**Framework**: Speech  
**Kind**: property

A Boolean value that determines whether a request must keep its audio data on the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var requiresOnDeviceRecognition: Bool { get set }
```

#### Discussion

Set this property to `true` to prevent an [`SFSpeechRecognitionRequest`](sfspeechrecognitionrequest.md) from sending audio over the network. However, on-device requests won’t be as accurate.

> **Note**:  The request only honors this setting if the [`supportsOnDeviceRecognition`](sfspeechrecognizer/supportsondevicerecognition.md) ([`SFSpeechRecognizer`](sfspeechrecognizer.md)) property is also `true`.

## See Also

- [var shouldReportPartialResults: Bool](sfspeechrecognitionrequest/shouldreportpartialresults.md)
  A Boolean value that indicates whether you want intermediate results returned for each utterance.
- [var contextualStrings: [String]](sfspeechrecognitionrequest/contextualstrings.md)
  An array of phrases that should be recognized, even if they are not in the system vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/requiresondevicerecognition)*