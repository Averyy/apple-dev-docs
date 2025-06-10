# SFSpeechRecognizerDelegate

**Framework**: Speech  
**Kind**: protocol

A protocol that you adopt in your objects to track the availability of a speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
protocol SFSpeechRecognizerDelegate : NSObjectProtocol
```

#### Overview

A speech recognizer’s availability can change due to the device’s Internet connection or other factors. Use this protocol’s optional method to track those changes and provide an appropriate response. For example, when speech recognition becomes unavailable, you might disable related features in your app.

## Topics

### Monitoring speech recognizer availability
- [func speechRecognizer(SFSpeechRecognizer, availabilityDidChange: Bool)](sfspeechrecognizerdelegate/speechrecognizer(_:availabilitydidchange:).md)
  Tells the delegate that the availability of its associated speech recognizer changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [class SFSpeechRecognizer](sfspeechrecognizer.md)
  An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.
- [enum SFSpeechRecognitionTaskHint](sfspeechrecognitiontaskhint.md)
  The type of task for which you are using speech recognition.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerdelegate)*