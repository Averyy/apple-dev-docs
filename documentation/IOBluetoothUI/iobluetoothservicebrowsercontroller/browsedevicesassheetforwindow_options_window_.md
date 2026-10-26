# browseDevicesAsSheetForWindow:options:window:

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```objc
+ (IOReturn) browseDevicesAsSheetForWindow:(IOBluetoothSDPServiceRecord **) outRecord options:(IOBluetoothServiceBrowserControllerOptions) inOptions window:(NSWindow *) inWindow;
```

#### Return Value

IOReturn - * kIOReturnSuccess - on successful completion. * kCanceledErr - User canceled.

#### Discussion

This method will allocate and run the IOBluetoothServiceBrowserController browser window as a sheet for a window.

## Parameters

- `outRecord`: Pointer to a (IOBluetoothSDPServiceRecord *) object. This will get allocated and returned to the client if the user selects a service.
- `inOptions`: For future expansion. Currently no options defined.
- `inWindow`: The window to be used as the anchor of the sheet.

## See Also

### Type Methods
- [class func withServiceBrowserControllerRef(IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!](./withservicebrowsercontrollerref%28_%29.md)
  Method call to convert an IOBluetoothServiceBrowserControllerRef into an IOBluetoothServiceBrowserController *.
- [+ browseDevices:options:](./browsedevices_options_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/browsedevicesassheetforwindow:options:window:)*