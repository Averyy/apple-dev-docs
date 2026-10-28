# withServiceBrowserControllerRef(_:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Type Method

Method call to convert an IOBluetoothServiceBrowserControllerRef into an IOBluetoothServiceBrowserController *.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!
```

```objc
+ (IOBluetoothServiceBrowserController *) withServiceBrowserControllerRef:(IOBluetoothServiceBrowserControllerRef) serviceBrowserControllerRef;
```

## Return Value

Returns the IOBluetoothServiceBrowserController * for the given IOBluetoothServiceBrowserControllerRef.

## Parameters

- `serviceBrowserControllerRef`: IOBluetoothServiceBrowserControllerRef for which an IOBluetoothServiceBrowserController * is desired.

## See Also

### Type Methods
- [+ browseDevices:options:](./browsedevices_options_.md)
- [+ browseDevicesAsSheetForWindow:options:window:](./browsedevicesassheetforwindow_options_window_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/withservicebrowsercontrollerref(_:))*