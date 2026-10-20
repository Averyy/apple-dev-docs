# MediaDeviceExtension

**Framework**: Media Device  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the requirements of a media device extension that discovers, activates, and plays media on a remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
protocol MediaDeviceExtension : AppExtension
```

## Mentions

- [Creating a media device extension](./creating-a-media-device-extension.md)

#### Overview

The extension requires the `com.apple.developer.media-device-extension` entitlement. As part of this entitlement an ID for your protocol needs to be specified. This same identifier must also be declared in the extension’s Info.plist as the `UTTypeIdentifier`. If the identifier in the entitlement and Info.plist do not match, the extension will not be run. This ID value can be used by other apps that use the `AVSystemRouting` framework and which intend to make use of an extension of this type.

The display name of the extension is sourced from the value of the `UTTypeDescription` key in the extension’s Info.plist. It may be presented in user interfaces.

## Topics

### Instance Properties
- [var protocolType: UTType](./mediadeviceextension/protocoltype.md)
  The communication protocol that this extension implements.
- [var supportsSimultaneousSessions: Bool](./mediadeviceextension/supportssimultaneoussessions.md)
  Indicates whether the extension supports handling simultaneous media sessions via `MediaOutputSession`.
### Instance Methods
- [func activateDevice(MediaOutputDevice, session: MediaOutputSession, for: MediaOutputDevice.Capabilities)](./mediadeviceextension/activatedevice%28_,session,for%29.md)
  Called when the user activates a device via a user interface.
- [func changeVolume(by: Int, for: MediaOutputDevice)](./mediadeviceextension/changevolume%28by,for%29.md)
  Changes the volume by a specified number of increments for the specified device.
- [func connectUsingPairingCode(String?, to: MediaOutputDevice, session: MediaOutputSession)](./mediadeviceextension/connectusingpairingcode%28_,to,session%29.md)
  Called after the user has input their authorization into a user interface. Use the Security framework’s keychain to store any derived key material.
- [func deactivateDevice(MediaOutputDevice, session: MediaOutputSession)](./mediadeviceextension/deactivatedevice%28_,session%29.md)
  Called when the user deactivates a device via a user interface.
- [func isDeviceMuted(MediaOutputDevice) -> Bool](./mediadeviceextension/isdevicemuted%28_%29.md)
  Gets the current mute state for the specified device.
- [func muteDevice(MediaOutputDevice)](./mediadeviceextension/mutedevice%28_%29.md)
  Mutes the audio output for the specified device.
- [func sendData(Data, toApplication: String, session: MediaOutputSession)](./mediadeviceextension/senddata%28_,toapplication,session%29.md)
  Called when an app sends data to a remote application.
- [func setVolume(Float, for: MediaOutputDevice)](./mediadeviceextension/setvolume%28_,for%29.md)
  Sets the volume level for the specified device.
- [func startDeviceDiscovery()](./mediadeviceextension/startdevicediscovery%28%29.md)
  Called when a user action requires discovered devices to be displayed.
- [func startSession(MediaOutputSession, identifier: String?, url: URL)](./mediadeviceextension/startsession%28_,identifier,url%29.md)
  Called when media playback or a remote application should be started on a remote device.
- [func stopDeviceDiscovery()](./mediadeviceextension/stopdevicediscovery%28%29.md)
  Called when the user dismisses the UI element that is showing devices.
- [func stopSession(MediaOutputSession)](./mediadeviceextension/stopsession%28_%29.md)
  Called when the application stops media playback.
- [func volume(for: MediaOutputDevice) -> Float](./mediadeviceextension/volume%28for%29.md)
  Gets the current volume level for the specified device.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)
### Inherited By
- [RealtimeSampleHandling](./realtimesamplehandling.md)

## See Also

### Essentials
- [Creating a media device extension](./creating-a-media-device-extension.md)
  Provide a way for people to find, connect to, and control your media device by adding a device extension in your iOS app.
- [Routing media to third-party devices](../AVSystemRouting/routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [protocol MediaDeviceExtensionConfiguration](./mediadeviceextensionconfiguration.md)
  Configuration for the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension)*