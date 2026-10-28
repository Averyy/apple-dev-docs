# seizeDevice()

**Framework**: Core HID  
**Kind**: method  
**Role**: Instance Method

Attempt to obtain the device so that this client is the only active client.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func seizeDevice() throws
```

## Discussion

If successful, this client is the only one that receives notifications using [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](./monitornotifications%28reportidstomonitor,elementstomonitor%29.md), and the only one that can use certain functions to interact with the device. The device won’t be freed until the client that holds it is deinitialized. There must not be any outstanding calls when attempting to seize a device.

> **Throws**: [`HIDDeviceError`](../hiddeviceerror.md) if the attempt to seize the device is unsuccessful. Notably, [`HIDDeviceError.busy`](../hiddeviceerror/busy.md) is thrown if there are outstanding calls to [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](./monitornotifications%28reportidstomonitor,elementstomonitor%29.md), [`dispatchSetReportRequest(type:id:data:timeout:)`](./dispatchsetreportrequest%28type,id,data,timeout%29.md), [`dispatchGetReportRequest(type:id:timeout:)`](./dispatchgetreportrequest%28type,id,timeout%29.md), or [`updateElements(_:timeout:)`](./updateelements%28_,timeout%29.md); and [`HIDDeviceError.exclusiveAccess`](../hiddeviceerror/exclusiveaccess.md) is thrown if the device is currently seized by another client.

## See Also

### Interact with the device
- [func dispatchGetReportRequest(type: HIDReportType, id: HIDReportID?, timeout: Duration?) async throws -> Data](./dispatchgetreportrequest%28type,id,timeout%29.md)
  Send a get report request to the device over the transport.
- [func dispatchSetReportRequest(type: HIDReportType, id: HIDReportID?, data: Data, timeout: Duration?) async throws](./dispatchsetreportrequest%28type,id,data,timeout%29.md)
  Send a set report request to the device over the transport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/seizedevice())*