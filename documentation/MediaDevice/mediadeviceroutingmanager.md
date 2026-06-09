# MediaDeviceRoutingManager

**Framework**: Media Device  
**Kind**: class

An object used by a [`MediaDeviceExtension`](mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class MediaDeviceRoutingManager
```

## Topics

### Instance Methods
- [func activatedDevice(MediaOutputDevice, session: MediaOutputSession)](mediadeviceroutingmanager/activateddevice(_:session:).md)
  Notifies the system that a device has been successfully activated and is ready for use.
- [func discoveryFailed(MediaDeviceError)](mediadeviceroutingmanager/discoveryfailed(_:).md)
  Reports a discovery failure to the system, indicating that the extension was unable to search for devices.
- [func failedToActivateDevice(MediaOutputDevice, session: MediaOutputSession, error: MediaDeviceError)](mediadeviceroutingmanager/failedtoactivatedevice(_:session:error:).md)
  Reports a device activation failure to the system so it can inform the user and clean up the session.
- [func foundDevice(MediaOutputDevice)](mediadeviceroutingmanager/founddevice(_:).md)
  Notifies the system of a new media device, so it can be included in device lists for users to select.
- [func lostDevice(MediaOutputDevice)](mediadeviceroutingmanager/lostdevice(_:).md)
  Removes a device from the system’s device lists so users can no longer select it.
- [func receiveData(Data, fromApplication: String, session: MediaOutputSession)](mediadeviceroutingmanager/receivedata(_:fromapplication:session:).md)
  Delivers data received from a remote application to the system for processing.
- [func reportRealtimeSampleDeliveryKPIs(session: MediaOutputSession, metKPIs: Bool)](mediadeviceroutingmanager/reportrealtimesampledeliverykpis(session:metkpis:).md)
  Reports whether the realtime sample delivery session has met its quality KPIs.
- [func requestPairingCode(for: MediaOutputDevice, session: MediaOutputSession, reason: LocalizedStringResource, authorizationMethod: MediaOutputDevice.AuthorizationMethod)](mediadeviceroutingmanager/requestpairingcode(for:session:reason:authorizationmethod:).md)
  Presents a pairing user interface so the user can enter authorization credentials for a device.
- [func sessionFailed(MediaOutputSession, error: MediaDeviceError)](mediadeviceroutingmanager/sessionfailed(_:error:).md)
  Reports an unrecoverable session error to the system so it can end the session and inform the user.
- [func started<T>(application: String?, playbackControl: T, session: MediaOutputSession)](mediadeviceroutingmanager/started(application:playbackcontrol:session:).md)
  Notifies the system that a remote application has successfully started on the target device.
- [func updateDevices([MediaOutputDevice])](mediadeviceroutingmanager/updatedevices(_:).md)
  Notifies the system that one or more devices have changed state, so their information can be refreshed in device lists.
- [func volumeChanged(for: MediaOutputDevice)](mediadeviceroutingmanager/volumechanged(for:).md)
  Notifies the system that the volume state has changed on a remote device.
### Type Methods
- [static func routingManager(for: any MediaDeviceExtension) -> MediaDeviceRoutingManager](mediadeviceroutingmanager/routingmanager(for:).md)
  Returns the shared routing manager instance for a media device extension.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MediaOutputSession](mediaoutputsession.md)
  Represents a media output session for playing content on a remote device.
- [protocol RealtimeSampleHandling](realtimesamplehandling.md)
  A protocol that extends a media device extension to support realtime sample delivery.
- [struct MediaDeviceError](mediadeviceerror.md)
  An error returned by MediaDeviceExtension operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager)*