# Responding to audio route changes

**Framework**: AVFAudio

Observe audio session notifications to ensure that your app responds appropriately to route changes.

#### Overview

An important responsibility of [`AVAudioSession`](avaudiosession.md) is managing audio route changes. A route change occurs when the system adds or removes an audio input or output. Route changes occur for several reasons, including a user plugging in a pair of headphones, connecting a Bluetooth LE headset, or unplugging a USB audio interface. When these changes occur, the audio session reroutes audio signals accordingly and broadcasts a notification containing the details of the change to any registered observers.

An important behavior related to route changes occurs when a user plugs in or removes a pair of headphones (see Playing audio in [`Human Interface Guidelines`](https://developer.apple.com/design/human-interface-guidelines)). When users connect a pair of wired or wireless headphones, they’re implicitly indicating that audio playback should continue, but privately. They expect an app that’s currently playing media to continue playing without pause. However, when users  their headphones, they don’t want to automatically share what they’re listening to with others. Applications should respect this implicit privacy request and automatically pause playback when users disconnect their headphones.

> **Note**:  [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) monitors your app’s audio session and responds appropriately to route changes. When users connect headphones, playback continues as expected. When they disconnect their headphones, playback is automatically paused. To observe this player behavior, key-value observe the player’s [`rate`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/rate) property so that you can update your user interface as the player pauses playback.

##### Observe Route Changes

You can directly observe route change notifications posted by the audio session. This might be useful if you want the system to notify you when a user connects headphones so you can present an icon or message in the player interface.

To observe audio route changes, begin by registering to observe notifications of type [`routeChangeNotification`](avaudiosession/routechangenotification.md).

```swift
func setupNotifications() {
    // Get the default notification center instance.
    let nc = NotificationCenter.default
    nc.addObserver(self,
                   selector: #selector(handleRouteChange),
                   name: AVAudioSession.routeChangeNotification,
                   object: nil)
}

@objc func handleRouteChange(notification: Notification) {
    // To be implemented.
}
```

##### Respond to Route Changes

The posted [`Notification`](https://developer.apple.com/documentation/Foundation/Notification) object contains a populated user-information dictionary providing the details of the route change. Determine the reason for this change by retrieving the [`AVAudioSession.RouteChangeReason`](avaudiosession/routechangereason.md) value from the dictionary. When a user connects a new device, the reason is [`AVAudioSession.RouteChangeReason.newDeviceAvailable`](avaudiosession/routechangereason/newdeviceavailable.md), and when a user removes a device, the reason is [`AVAudioSession.RouteChangeReason.oldDeviceUnavailable`](avaudiosession/routechangereason/olddeviceunavailable.md).

When a new device becomes available, you ask the audio session for its [`currentRoute`](avaudiosession/currentroute.md) to determine where the audio output is currently routed. This query returns an [`AVAudioSessionRouteDescription`](avaudiosessionroutedescription.md) object that lists all of the audio session’s inputs and outputs. When the user removes a device, you retrieve the route description for the previous route from the user-information dictionary. In both cases, you query the route description for its outputs, which returns an array of port description objects providing the details of the audio output routes.

```swift
@objc func handleRouteChange(notification: Notification) {
    guard let userInfo = notification.userInfo,
        let reasonValue = userInfo[AVAudioSessionRouteChangeReasonKey] as? UInt,
        let reason = AVAudioSession.RouteChangeReason(rawValue: reasonValue) else {
            return
    }
    
    // Switch over the route change reason.
    switch reason {

    case .newDeviceAvailable: // New device found.
        let session = AVAudioSession.sharedInstance()
        headphonesConnected = hasHeadphones(in: session.currentRoute)
    
    case .oldDeviceUnavailable: // Old device removed.
        if let previousRoute =
            userInfo[AVAudioSessionRouteChangePreviousRouteKey] as? AVAudioSessionRouteDescription {
            headphonesConnected = hasHeadphones(in: previousRoute)
        }
    
    default: ()
    }
}

func hasHeadphones(in routeDescription: AVAudioSessionRouteDescription) -> Bool {
    // Filter the outputs to only those with a port type of headphones.
    return !routeDescription.outputs.filter({$0.portType == .headphones}).isEmpty
}
```

## See Also

- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md)
  Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioSession](avaudiosession.md)
  An object that communicates to the system how you intend to use audio in your app.
- [class AVAudioApplication](avaudioapplication.md)
  An object that manages one or more audio sessions that belong to an app.
- [class AVAudioRoutingArbiter](avaudioroutingarbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/responding-to-audio-route-changes)*