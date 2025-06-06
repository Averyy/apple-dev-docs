# SFSpeechRecognizerDelegate

**Framework**: Speech  
**Kind**: protocol

A protocol that you adopt in your objects to track the availability of a speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
protocol SFSpeechRecognizerDelegate : NSObjectProtocol
```

#### Overview

A speech recognizer’s availability can change due to the device’s Internet connection or other factors. Use this protocol’s optional method to track those changes and provide an appropriate response. For example, when speech recognition becomes unavailable, you might disable related features in your app.

## Topics

### Monitoring the Availability of a Speech Recognizer
- [func speechRecognizer(SFSpeechRecognizer, availabilityDidChange: Bool)](sfspeechrecognizerdelegate/speechrecognizer(_:availabilitydidchange:).md)
  Tells the delegate that the availability of its associated speech recognizer changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SFSpeechRecognizerDelegate)?](sfspeechrecognizer/delegate.md)
  The delegate object that handles changes to the availability of speech recognition services.
- [var isAvailable: Bool](sfspeechrecognizer/isavailable.md)
  A Boolean value that indicates whether the speech recognizer is currently available.
- [var supportsOnDeviceRecognition: Bool](sfspeechrecognizer/supportsondevicerecognition.md)
  A Boolean value that indicates whether the speech recognizer can operate without network access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerdelegate)*