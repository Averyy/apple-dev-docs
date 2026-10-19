# NSSpeechRecognitionUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is requesting to send user data to Apple’s speech recognition servers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.15+
- visionOS 1.0+



**Type**: string

#### Discussion

> ❗ **Important**:  Include this key if your app uses the Speech framework. This applies regardless of whether you set [`requiresOnDeviceRecognition`](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/requiresondevicerecognition) to `true` or `false`. If this key isn’t present, your app crashes when it calls [`requestAuthorization(_:)`](https://developer.apple.com/documentation/speech/sfspeechrecognizer/requestauthorization(_:)).

## See Also

- [Asking Permission to Use Speech Recognition](../speech/asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsspeechrecognitionusagedescription)*