# init(audioSession:)

**Framework**: Core Haptics  
**Kind**: init

Creates a haptic engine from an audio session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(audioSession: AVAudioSession?) throws
```

#### Discussion

Create your haptic engine with this initializer if you want the audio behavior of your engine to match other audio APIs in your app. For example, if you’re using [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) to manage audio elsewhere in your app, then you want to share the session’s [`sharedInstance()`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/sharedInstance()). In this case, the engine mutes and routes audio in accordance with the passed session.

Otherwise, if you don’t pass it a session, it won’t behave the same way as elsewhere in app; audio behaves like [`UIKit`](https://developer.apple.com/documentation/UIKit), without syncing to a specific session. You should pass `nil` when you need the engine only for playing haptics.

## Parameters

- `audioSession`: The shared audio session, if you’re already using one in your app, to sync with the created engine. For example, pass in   if you’re using audio from  . Pass in   to use default   audio behavior.

## See Also

- [init() throws](chhapticengine/init.md)
  Creates an instance of the haptic engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/init(audiosession:))*