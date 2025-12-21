# Hearing device support

**Framework**: Accessibility

Access information about paired hearing aid devices and streaming status.

#### Overview

Companion apps for hearing device manufacturers might offer certain features, like remote fitting and hearing device health checks, that rely on streaming audio to the hearing devices. If a user disables audio streaming on their Apple device, these features might become unavailable.

This API gives your app the ability to check the state of the streaming preferences, so you can ask users to temporarily enable streaming to use your app’s features. You can also query other information about streaming capabilities and paired hearing devices.

Use this API to check:

- The state of the streaming preferences for the hearing device in each ear
- Whether the iOS device supports bidirectional streaming
- The Bluetooth UUIDs of the paired hearing devices that match your app’s `hearing.aid.app` entitlement

## Topics

### Hearing devices
- [struct AXMFiHearingDevice](axmfihearingdevice.md)
  A namespace for hearing device accessibility symbols in Swift.
### Streaming status
- [AXMFiHearingDevice.Ear](axmfihearingdevice/ear.md)
  Constants that represent a hearing device ear.
- [static func streamingEar() -> AXMFiHearingDevice.Ear](axmfihearingdevice/streamingear.md)
  Returns which ears enable streaming.
- [static let streamingEarDidChangeNotification: NSNotification.Name](axmfihearingdevice/streamingeardidchangenotification.md)
  A notification that the system posts when there’s a change to which ears enable streaming.
### Streaming type
- [static func supportsBidirectionalStreaming() -> Bool](axmfihearingdevice/supportsbidirectionalstreaming.md)
  Returns a Boolean value that indicates whether the iOS device supports bidirectional streaming.
### Paired hearing devices
- [static func pairedDeviceIdentifiers() -> [UUID]](axmfihearingdevice/paireddeviceidentifiers.md)
  Returns the UUIDs of the hearing device peripherals.
- [static let pairedUUIDsDidChangeNotification: NSNotification.Name](axmfihearingdevice/paireduuidsdidchangenotification.md)
  A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.

## See Also

- [Customized accessibility content](customized-accessibility-content.md)
  Customize your apps to deliver accessibility information to your users in measured portions as they need it.
- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [func AXNameFromColor(CGColor) -> String](axnamefromcolor(_:).md)
  Returns a localized description of the color to use in accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/hearing-device-support)*