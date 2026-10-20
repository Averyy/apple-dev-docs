# kColorSyncPrinterDeviceClass

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The device class for a printer device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncPrinterDeviceClass;
```

#### Discussion

The string that represents a printer device is `prtr`.

## See Also

### Identifying device classes
- [var kColorSyncCameraDeviceClass: Unmanaged<CFString>!](./kcolorsynccameradeviceclass.md)
  The device class for a camera device.
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](./kcolorsyncdeviceclass.md)
  A key whose value is one of the device-class constants below.
- [var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!](./kcolorsyncdisplaydeviceclass.md)
  The device class for a display device.
- [var kColorSyncScannerDeviceClass: Unmanaged<CFString>!](./kcolorsyncscannerdeviceclass.md)
  The device class for a scanner device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncprinterdeviceclass)*