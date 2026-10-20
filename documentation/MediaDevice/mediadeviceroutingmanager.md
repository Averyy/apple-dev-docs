# MediaDeviceRoutingManager

**Framework**: Media Device  
**Kind**: class  
**Role**: Class

An object used by a [`MediaDeviceExtension`](./mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final class MediaDeviceRoutingManager
```

## Topics

### Instance Methods
- [func activatedDevice(MediaOutputDevice, session: MediaOutputSession)](./mediadeviceroutingmanager/activateddevice%28_,session%29.md)
  Notifies the system that a device has been successfully activated and is ready for use.
- [func discoveryFailed(MediaDeviceError)](./mediadeviceroutingmanager/discoveryfailed%28_%29.md)
  Reports a discovery failure to the system, indicating that the extension was unable to search for devices.
- [func failedToActivateDevice(MediaOutputDevice, session: MediaOutputSession, error: MediaDeviceError)](./mediadeviceroutingmanager/failedtoactivatedevice%28_,session,error%29.md)
  Reports a device activation failure to the system so it can inform the user and clean up the session.
- [func foundDevice(MediaOutputDevice)](./mediadeviceroutingmanager/founddevice%28_%29.md)
  Notifies the system of a new media device, so it can be included in device lists for users to select.
- [func lostDevice(MediaOutputDevice)](./mediadeviceroutingmanager/lostdevice%28_%29.md)
  Removes a device from the system’s device lists so users can no longer select it.
- [func receiveData(Data, fromApplication: String, session: MediaOutputSession)](./mediadeviceroutingmanager/receivedata%28_,fromapplication,session%29.md)
  Delivers data received from a remote application to the system for processing.
- [func reportQualityMetricsPassed(Bool, forSession: MediaOutputSession)](./mediadeviceroutingmanager/reportqualitymetricspassed%28_,forsession%29.md)
  Reports whether the realtime sample delivery session has met its quality KPIs.
- [func requestPairingCode(for: MediaOutputDevice, session: MediaOutputSession, reason: LocalizedStringResource, authorizationMethod: MediaOutputDevice.AuthorizationMethod)](./mediadeviceroutingmanager/requestpairingcode%28for,session,reason,authorizationmethod%29.md)
  Presents a pairing user interface so the user can enter authorization credentials for a device.
- [func sessionFailed(MediaOutputSession, error: MediaDeviceError)](./mediadeviceroutingmanager/sessionfailed%28_,error%29.md)
  Reports an unrecoverable session error to the system so it can end the session and inform the user.
- [func started<T>(application: String?, playbackControl: T, session: MediaOutputSession)](./mediadeviceroutingmanager/started%28application,playbackcontrol,session%29.md)
  Notifies the system that a remote application has successfully started on the target device.
- [func updateDevices([MediaOutputDevice])](./mediadeviceroutingmanager/updatedevices%28_%29.md)
  Notifies the system that one or more devices have changed state, so their information can be refreshed in device lists.
- [func volumeChanged(for: MediaOutputDevice)](./mediadeviceroutingmanager/volumechanged%28for%29.md)
  Notifies the system that the volume state has changed on a remote device.
### Type Methods
- [static func routingManager(for: any MediaDeviceExtension) -> MediaDeviceRoutingManager](./mediadeviceroutingmanager/routingmanager%28for%29.md)
  Returns the shared routing manager instance for a media device extension.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Session and system communication
- [class MediaOutputSession](./mediaoutputsession.md)
  Represents a media output session for playing content on a remote device.
- [protocol RealtimeSampleHandling](./realtimesamplehandling.md)
  A protocol that extends a media device extension to support realtime sample delivery.
- [struct MediaDeviceError](./mediadeviceerror.md)
  An error returned by MediaDeviceExtension operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager)*