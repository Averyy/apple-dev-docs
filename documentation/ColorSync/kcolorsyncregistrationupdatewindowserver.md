# kColorSyncRegistrationUpdateWindowServer

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

A notification concerning the window server’s device registration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncRegistrationUpdateWindowServer: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncRegistrationUpdateWindowServer;
```

## See Also

### Observing device notifications
- [var kColorSyncDeviceProfilesNotification: Unmanaged<CFString>!](./kcolorsyncdeviceprofilesnotification.md)
  A notification that ColorSync posts when a device’s profiles change.
- [var kColorSyncDeviceRegisteredNotification: Unmanaged<CFString>!](./kcolorsyncdeviceregisterednotification.md)
  A notification that ColorSync posts when a device is registered.
- [var kColorSyncDeviceUnregisteredNotification: Unmanaged<CFString>!](./kcolorsyncdeviceunregisterednotification.md)
  A notification that ColorSync posts when a device is unregistered.
- [var kColorSyncDisplayDeviceProfilesNotification: Unmanaged<CFString>!](./kcolorsyncdisplaydeviceprofilesnotification.md)
  A notification that ColorSync posts when a display device’s profiles change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncregistrationupdatewindowserver)*