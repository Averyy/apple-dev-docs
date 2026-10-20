# kColorSyncDisplayDeviceClass

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The device class for a display device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncDisplayDeviceClass;
```

#### Discussion

The string that represents a display device is `mntr`.

## See Also

### Identifying device classes
- [var kColorSyncCameraDeviceClass: Unmanaged<CFString>!](./kcolorsynccameradeviceclass.md)
  The device class for a camera device.
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](./kcolorsyncdeviceclass.md)
  A key whose value is one of the device-class constants below.
- [var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!](./kcolorsyncprinterdeviceclass.md)
  The device class for a printer device.
- [var kColorSyncScannerDeviceClass: Unmanaged<CFString>!](./kcolorsyncscannerdeviceclass.md)
  The device class for a scanner device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdisplaydeviceclass)*