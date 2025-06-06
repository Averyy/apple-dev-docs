# speechRecognizer(_:availabilityDidChange:)

**Framework**: Speech  
**Kind**: method

Tells the delegate that the availability of its associated speech recognizer changed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognizer(_ speechRecognizer: SFSpeechRecognizer, availabilityDidChange available: Bool)
```

## Parameters

- `speechRecognizer`: The   object whose availability changed.
- `available`: A Boolean value that indicates the new availability of the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerdelegate/speechrecognizer(_:availabilitydidchange:))*