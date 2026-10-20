# kColorSyncDeviceUnregisteredNotification

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

A notification that ColorSync posts when a device is unregistered.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncDeviceUnregisteredNotification: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncDeviceUnregisteredNotification;
```

## See Also

### Observing device notifications
- [var kColorSyncDeviceProfilesNotification: Unmanaged<CFString>!](./kcolorsyncdeviceprofilesnotification.md)
  A notification that ColorSync posts when a device’s profiles change.
- [var kColorSyncDeviceRegisteredNotification: Unmanaged<CFString>!](./kcolorsyncdeviceregisterednotification.md)
  A notification that ColorSync posts when a device is registered.
- [var kColorSyncDisplayDeviceProfilesNotification: Unmanaged<CFString>!](./kcolorsyncdisplaydeviceprofilesnotification.md)
  A notification that ColorSync posts when a display device’s profiles change.
- [var kColorSyncRegistrationUpdateWindowServer: Unmanaged<CFString>!](./kcolorsyncregistrationupdatewindowserver.md)
  A notification concerning the window server’s device registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdeviceunregisterednotification)*