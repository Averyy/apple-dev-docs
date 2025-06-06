# AVAudioRoutingArbiter

**Framework**: AVFAudio  
**Kind**: class

An object for configuring macOS apps to participate in AirPods Automatic Switching.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class AVAudioRoutingArbiter
```

#### Overview

AirPods Automatic Switching is a feature of Apple operating systems that intelligently connects wireless headphones to the most appropriate audio device in a multidevice environment. For example, if a user plays a movie on iPad, and then locks the device and starts playing music on iPhone, the system automatically switches the source audio device from iPad to iPhone.

iOS apps automatically participate in AirPods Automatic Switching. To enable your macOS app to participate in this behavior, use `AVAudioRoutingArbiter` to indicate when your app starts and finishes playing or recording audio. For example, a Voice over IP (VoIP) app might request arbitration before starting a call, and when the arbitration completes, begin the VoIP session. Likewise, when the call ends, the app would end the VoIP session and leave arbitration.

```swift
func startCall() {
    let arbiter = AVAudioRoutingArbiter.shared
    arbiter.begin(category: .playAndRecordVoice) { deviceChanged, error in
        // Start VoIP session.
    }
}

func endCall() {
    // End VoIP session.
    AVAudioRoutingArbiter.shared.leave()
}
```

> ❗ **Important**:  Only certain Apple and Beats wireless headsets support this feature.

 Only certain Apple and Beats wireless headsets support this feature.

## Topics

### Creating a Routing Arbiter
- [class var shared: AVAudioRoutingArbiter](avaudioroutingarbiter/shared.md)
  The shared routing arbiter object.
### Participating in AirPods Automatic Switching
- [func begin(category: AVAudioRoutingArbiter.Category, completionHandler: (Bool, (any Error)?) -> Void)](avaudioroutingarbiter/begin(category:completionhandler:).md)
  Begins routing arbitration to take ownership of a nearby Bluetooth audio route.
- [AVAudioRoutingArbiter.Category](avaudioroutingarbiter/category.md)
  Categories that describe the general nature of your app’s audio use.
- [func leave()](avaudioroutingarbiter/leave.md)
  Stops an app’s participation in audio routing arbitration.

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
- [class AVAudioApplication](avaudioapplication.md)
  An object that manages one or more audio sessions that belong to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioroutingarbiter)*