# requestAuthorization(_:)

**Framework**: Speech  
**Kind**: method

Asks the user to allow your app to perform speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func requestAuthorization(_ handler: @escaping (SFSpeechRecognizerAuthorizationStatus) -> Void)
```

## Mentions

- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)

#### Discussion

Call this method before performing any other tasks associated with speech recognition. This method executes asynchronously, returning shortly after you call it. At some point later, the system calls the provided `handler` block with the results.

When your app’s authorization status is [`SFSpeechRecognizerAuthorizationStatus.notDetermined`](sfspeechrecognizerauthorizationstatus/notdetermined.md), this method causes the system to prompt the user to grant or deny permission for your app to use speech recognition. The prompt includes the custom message you specify in the `NSSpeechRecognitionUsageDescription` key of your app’s `Info.plist` file. The user’s response is saved so that future calls to this method do not prompt the user again.

> ❗ **Important**:  Your app’s `Info.plist` file must contain the `NSSpeechRecognitionUsageDescription` key with a valid usage description. If this key is not present, your app will crash when you call this method.

 Your app’s `Info.plist` file must contain the `NSSpeechRecognitionUsageDescription` key with a valid usage description. If this key is not present, your app will crash when you call this method.

For more information about requesting authorization, see [`Asking Permission to Use Speech Recognition`](asking-permission-to-use-speech-recognition.md).

## Parameters

- `handler`: The block to execute when your app’s authorization status is known. The status parameter of the block contains your app’s authorization status. The system does not guarantee the execution of this block on your app’s main dispatch queue.

## See Also

- [class func authorizationStatus() -> SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizer/authorizationstatus.md)
  Returns your app’s current authorization to perform speech recognition.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/requestauthorization(_:))*