# AVAudioApplication

**Framework**: AVFAudio  
**Kind**: class

An object that manages one or more audio sessions that belong to an app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class AVAudioApplication
```

#### Overview

Access the shared audio application instance to control app-level audio operations, such as requesting microphone permission and controlling audio input muting.

## Topics

### Accessing the shared instance
- [class var shared: AVAudioApplication](avaudioapplication/shared.md)
  Accesses the shared audio application instance.
### Requesting audio recording permission
- [class func requestRecordPermission(completionHandler: (Bool) -> Void)](avaudioapplication/requestrecordpermission(completionhandler:).md)
  Determines whether the app has permission to record audio.
- [var recordPermission: AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.property.md)
  The app’s permission to record audio.
- [AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.enum.md)
  Constants that indicate the app’s permission to record audio.
### Requesting microphone injection permission
- [class func requestMicrophoneInjectionPermission(completionHandler: (AVAudioApplication.MicrophoneInjectionPermission) -> Void)](avaudioapplication/requestmicrophoneinjectionpermission(completionhandler:).md)
  Requests the app’s permission to add audio to calls.
- [var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.property.md)
  A value that indicates an app’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.enum.md)
  Constants that indicate an app’s permission to add audio to calls.
### Managing audio input mute state
- [var isInputMuted: Bool](avaudioapplication/isinputmuted.md)
  A Boolean value that indicates whether the app’s audio input is in a muted state.
- [func setInputMuted(Bool) throws](avaudioapplication/setinputmuted(_:).md)
  Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [class let inputMuteStateChangeNotification: NSNotification.Name](avaudioapplication/inputmutestatechangenotification.md)
  A notification the system posts when the app’s audio input mute state changes.
- [func setInputMuteStateChangeHandler(((Bool) -> Bool)?) throws](avaudioapplication/setinputmutestatechangehandler(_:).md)
  Sets a callback to handle changes to application-level audio muting states.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md)
  Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioSession](avaudiosession.md)
  An object that communicates to the system how you intend to use audio in your app.
- [class AVAudioRoutingArbiter](avaudioroutingarbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication)*