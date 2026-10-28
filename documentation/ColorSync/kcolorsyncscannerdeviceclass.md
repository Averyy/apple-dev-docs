# kColorSyncScannerDeviceClass

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The device class for a scanner device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncScannerDeviceClass: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncScannerDeviceClass;
```

## Discussion

The string that represents a scanner device is `scnr`.

## See Also

### Identifying device classes
- [var kColorSyncCameraDeviceClass: Unmanaged<CFString>!](./kcolorsynccameradeviceclass.md)
  The device class for a camera device.
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](./kcolorsyncdeviceclass.md)
  A key whose value is one of the device-class constants below.
- [var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!](./kcolorsyncdisplaydeviceclass.md)
  The device class for a display device.
- [var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!](./kcolorsyncprinterdeviceclass.md)
  The device class for a printer device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncscannerdeviceclass)*