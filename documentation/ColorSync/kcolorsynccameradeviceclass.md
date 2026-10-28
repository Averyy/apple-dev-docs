# kColorSyncCameraDeviceClass

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The device class for a camera device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncCameraDeviceClass: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncCameraDeviceClass;
```

## Discussion

The string that represents a camera device is `cmra`.

## See Also

### Identifying device classes
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](./kcolorsyncdeviceclass.md)
  A key whose value is one of the device-class constants below.
- [var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!](./kcolorsyncdisplaydeviceclass.md)
  The device class for a display device.
- [var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!](./kcolorsyncprinterdeviceclass.md)
  The device class for a printer device.
- [var kColorSyncScannerDeviceClass: Unmanaged<CFString>!](./kcolorsyncscannerdeviceclass.md)
  The device class for a scanner device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynccameradeviceclass)*