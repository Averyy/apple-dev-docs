# browseDevices:options:

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```objc
+ (IOReturn) browseDevices:(IOBluetoothSDPServiceRecord **) outRecord options:(IOBluetoothServiceBrowserControllerOptions) inOptions;
```

#### Return Value

IOReturn - * kIOReturnSuccess - on successful completion. * kCanceledErr - User canceled.

#### Discussion

This method allocates and runs the browser window as a modal window waiting for the user to either select a service, or cancel the browser window.

## Parameters

- `outRecord`: Pointer to a (IOBluetoothSDPServiceRecord *) object. This will get allocated and returned to the client if the user selects a service.
- `inOptions`: For future expansion. Currently no options defined.

## See Also

### Type Methods
- [class func withServiceBrowserControllerRef(IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!](./withservicebrowsercontrollerref%28_%29.md)
  Method call to convert an IOBluetoothServiceBrowserControllerRef into an IOBluetoothServiceBrowserController *.
- [+ browseDevicesAsSheetForWindow:options:window:](./browsedevicesassheetforwindow_options_window_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/browsedevices:options:)*