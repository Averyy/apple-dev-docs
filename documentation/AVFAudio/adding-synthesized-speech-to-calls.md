# Adding synthesized speech to calls

**Framework**: AVFAudio

Provide a more accessible experience by adding your app’s audio to a call.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Xcode 16.1+

#### Overview

This sample shows how to create an accessibility app that supports augmentative and alternative communication (AAC) by adding synthesized speech to a call. This feature is available in iOS 18.2 and visionOS 2.2 and later, and is available to use with calling apps that capture microphone input using Apple’s voice processing like Phone, FaceTime, and most VoIP apps.

The sample app provides a basic user interface with a button to toggle the feature state and a text field. When you enter text into the field and press enter, the app speaks the phrase. If you have an active call in progress and you enable adding the app’s audio to it, you’ll hear the synthesized speech on the originating and receiving ends of the call.

#### Configure the Sample Code Project

The sample requires running on an iOS device with iOS 18.2 or later. To test the sample, establish a phone or FaceTime call with another device.

#### Enable the Accessibility Service

Before an app can add its audio to calls, a person must turn on a system-level service in the Settings app by choosing Accessibility > Audio & Visual > Add Audio in Calls. This setting is global to the device and influences the availability of the service for all apps.

![A screenshot showing the Add Audio in Calls screen in the Settings app. At the top of the image is a navigation bar title of Add Audio in Calls and a Back button on its leading edge. Below the navigation bar is a toggle switch, in an enabled state, with the label of Allow Apps to Add Audio in Calls. Below the switch is a description of this feature with the text Any audio from apps, along with microphone input, will be audible during a call. Muting the microphone will silence all audio. This may be used by apps that help assist with speaking and communication.](https://docs-assets.developer.apple.com/published/794d40aef207b215a4d7518067f6713d/add_audio_in_calls%402x.png)

The sample determines the state of this setting by querying the shared [`AVAudioApplication`](avaudioapplication.md) object for its microphone injection permission:

```swift
// Retrieve the current microphone injection permission.
let permission = AVAudioApplication.shared.microphoneInjectionPermission
```

A permission value of [`AVAudioApplication.MicrophoneInjectionPermission.serviceDisabled`](avaudioapplication/microphoneinjectionpermission-swift.enum/servicedisabled.md) indicates the person hasn’t turned on the service, which means apps can’t add audio to calls. When the app retrieves this value, it presents an alert dialog that indicates the current state and provides the person an opportunity to update their setting. When you press the dialog’s Open Settings button, the app uses the Accessibility framework to directly open the Add Audio in Calls screen in the Settings app like shown below.

```swift
@ViewBuilder
var alertButtons: some View {
    Button("Open Settings") {
        Task {
            do {
                // Open the configuration screen for this feature in the Settings app.
                try await AccessibilitySettings.openSettings(for: .allowAppsToAddAudioToCalls)
            } catch {
                print("Unable to open Settings app: \(error)")
            }
        }
    }
    Button("Cancel", role: .cancel) {}
}
```

#### Request Permission

Turning on Add Audio in Calls makes the feature available to apps on the system, but apps must explicitly request and be granted permission to use the feature. The sample determines its permission by querying for the current microphone injection permission. A value of [`AVAudioApplication.MicrophoneInjectionPermission.undetermined`](avaudioapplication/microphoneinjectionpermission-swift.enum/undetermined.md) indicates the app hasn’t yet requested permission and needs to before it can use the feature.

For an app to request a person’s permission, it needs to provide an `NSMicrophoneInjectionUsageDescription` key in its `Info.plist` file with a description of why the app requests microphone access. The system displays this string when an app requests user permission. The sample app defines this entry as follows.

```swift
<key>NSMicrophoneInjectionUsageDescription</key>
<string>This app adds its audio to calls to support augmentative and alternative communication.</string>
```

Attempting to request permission without this usage string present results in the system quitting the app.

The app requests permission by calling the  [`requestRecordPermission(completionHandler:)`](avaudioapplication/requestrecordpermission(completionhandler:).md) method and awaiting a response:

```swift
// If undetermined, prompt the person to grant the app access, and turn on the feature, if allowed.
if await AVAudioApplication.requestMicrophoneInjectionPermission() == .granted {
    // If the person grants access, turn on adding app audio.
}
```

Calling this method causes the system to present a dialog that requests user permission. If a person grants the app permission, the call returns a value of [`AVAudioApplication.MicrophoneInjectionPermission.granted`](avaudioapplication/microphoneinjectionpermission-swift.enum/granted.md) and the app updates its state accordingly.

If a person denies the app permission, the system sets the microphone injection permission state to [`AVAudioApplication.MicrophoneInjectionPermission.denied`](avaudioapplication/microphoneinjectionpermission-swift.enum/denied.md), and the app is unable to use the feature. The app remains in this state until a person explicitly changes the permission from the Add Audio in Calls screen in the Settings app. If you attempt to turn on the feature in the app while in this state, the app presents an alert similar to the one shown in the previous section to update the app’s permission.

#### Enable Adding Audio to Calls

When the app has permission to add audio and a person toggles the feature state in the user interface, the app responds by calling the shared [`AVAudioSession`](avaudiosession.md) object’s [`setPreferredMicrophoneInjectionMode(_:)`](avaudiosession/setpreferredmicrophoneinjectionmode(_:).md) method. To turn on the feature, the app passes the method a value of [`AVAudioSession.MicrophoneInjectionMode.spokenAudio`](avaudiosession/microphoneinjectionmode/spokenaudio.md); to turn off the feature, it passes a value of [`AVAudioSession.MicrophoneInjectionMode.none`](avaudiosession/microphoneinjectionmode/none.md).

```swift
let mode: AVAudioSession.MicrophoneInjectionMode = // spoken audio or none
try AVAudioSession.sharedInstance().setPreferredMicrophoneInjectionMode(mode)
```

When turned on during an active call, the system plays the app’s audio locally and adds it to the microphone’s input stream.

> **Note**: The `AVAudioSession/setPreferredMicrophoneInjectionMode(_:)` method uses the word  to indicate that an app can set its preference, but a person ultimately determines whether they allow the feature’s use.

The `AVAudioSession/setPreferredMicrophoneInjectionMode(_:)` method uses the word  to indicate that an app can set its preference, but a person ultimately determines whether they allow the feature’s use.

#### Monitor the Availability of Calls

To determine whether a call can use this feature, the sample awaits notification of changes to the state of the audio session’s microphone injection capabilities:

```swift
/// Monitor the active state of phone and FaceTime calls.
private func observeCallState() async {
    // Await notification of changes to the audio session's microphone injection capabilities.
    for await notification in NotificationCenter.default.notifications(named: AVAudioSession.microphoneInjectionCapabilitiesChangeNotification) {
        // Inspect the user information dictionary to determine whether microphone injection is available.
        isCallActive = notification.userInfo?[AVAudioSessionMicrophoneInjectionIsAvailableKey] as? Bool ?? false
    }
}
```

When a call begins or ends, the system posts a notification of the change. The app queries the notification’s user information dictionary for its [`AVAudioSessionMicrophoneInjectionIsAvailableKey`](avaudiosessionmicrophoneinjectionisavailablekey.md) value to determine whether there’s an active call. When the value is `true`, the app updates its UI to show a pulsing phone icon in the toolbar to indicate the call is active.

## See Also

- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioSession](avaudiosession.md)
  An object that communicates to the system how you intend to use audio in your app.
- [class AVAudioApplication](avaudioapplication.md)
  An object that manages one or more audio sessions that belong to an app.
- [class AVAudioRoutingArbiter](avaudioroutingarbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/adding-synthesized-speech-to-calls)*