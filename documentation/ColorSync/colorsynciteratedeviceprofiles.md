# ColorSyncIterateDeviceProfiles(_:_:)

**Framework**: ColorSync  
**Kind**: func

Iterates over the profiles registered for all devices, invoking a callback for each.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback!, _ userInfo: UnsafeMutableRawPointer?)
```

## Parameters

- `callBack`: The callback to invoke for each registered device profile.
- `userInfo`: Caller-supplied context passed through to the callback. Optional.

## See Also

- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
  Copies information about a device, resolved for the current host and current user.
- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
  A callback that ColorSync invokes for each device profile during iteration.
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncdevicesetcustomprofiles(_:_:_:).md)
  Sets custom profiles for a device in lieu of its factory profiles.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatedeviceprofile(_:_:_:).md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncregisterdevice(_:_:_:).md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciteratedeviceprofiles(_:_:))*