# init(id:displayName:capabilities:canGroupWithCurrentlyActivatedDevices:deviceType:volumeControl:canMute:requiredNetworkEndpoints:txtRecords:supportsSimultaneousSessions:)

**Framework**: Media Device  
**Kind**: init

Creates a new media output device with the specified properties, requiring at least one network endpoint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init?(id: UUID, displayName: String, capabilities: MediaOutputDevice.Capabilities, canGroupWithCurrentlyActivatedDevices: Bool = true, deviceType: MediaOutputDevice.DeviceType = .tv, volumeControl: MediaOutputDevice.VolumeControl = .relative, canMute: Bool = true, requiredNetworkEndpoints networkEndpoints: [NWEndpoint], txtRecords: [NWTXTRecord] = [], supportsSimultaneousSessions: Bool = false)
```

#### Return Value

A configured `MediaOutputDevice`, or `nil` if `networkEndpoints` is empty.

#### Discussion

This is the preferred initializer for [`MediaOutputDevice`](mediaoutputdevice.md). It enforces that the device has at least one valid network endpoint, returning `nil` if the `networkEndpoints` array is empty. Devices discovered via network browsing (e.g., Bonjour/mDNS) should always have associated endpoints, and this initializer ensures that invariant at construction time.

## Parameters

- `id`: A unique identifier for the device. This value is used for equality checks and hashing.
- `displayName`: A human-readable name for the device, presented in system user interfaces such as the media output picker.
- `capabilities`: The set of media capabilities the device supports, such as real-time audio/video streaming, URL playback, or application launch.
- `canGroupWithCurrentlyActivatedDevices`: Whether this device can be added to a group with other currently active devices via `MediaDeviceExtension/activateDevice(_:for:)`. Defaults to `true`.
- `deviceType`: The type of device, which determines the icon shown in user interfaces. Defaults to `.tv`.
- `volumeControl`: The type of volume control the device supports. Defaults to `.absolute`.
- `canMute`: Whether the device supports muting audio output. Defaults to `true`.
- `networkEndpoints`: The network endpoints used to communicate with this device. Must contain at least one endpoint or the initializer returns `nil`.
- `txtRecords`: TXT records containing device metadata discovered via network protocols. Defaults to an empty array.
- `supportsSimultaneousSessions`: Whether the device supports receiving multiple concurrent media sessions via [`MediaOutputSession`](mediaoutputsession.md). Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/init(id:displayname:capabilities:cangroupwithcurrentlyactivateddevices:devicetype:volumecontrol:canmute:requirednetworkendpoints:txtrecords:supportssimultaneoussessions:))*