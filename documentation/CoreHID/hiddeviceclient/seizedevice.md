# seizeDevice()

**Framework**: Core HID  
**Kind**: method

Attempt to obtain the device so that this client is the only active client.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func seizeDevice() throws
```

#### Discussion

If successful, this client is the only one that receives notifications using [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md), and the only one that can use certain functions to interact with the device. The device won’t be freed until the client that holds it is deinitialized. There must not be any outstanding calls when attempting to seize a device.

> **Note**: [`HIDDeviceError`](hiddeviceerror.md) if the attempt to seize the device is unsuccessful. Notably, [`HIDDeviceError.busy`](hiddeviceerror/busy.md) is thrown if there are outstanding calls to [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md), [`dispatchSetReportRequest(type:id:data:timeout:)`](hiddeviceclient/dispatchsetreportrequest(type:id:data:timeout:).md), [`dispatchGetReportRequest(type:id:timeout:)`](hiddeviceclient/dispatchgetreportrequest(type:id:timeout:).md), or [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md); and [`HIDDeviceError.exclusiveAccess`](hiddeviceerror/exclusiveaccess.md) is thrown if the device is currently seized by another client.

## See Also

- [func dispatchGetReportRequest(type: HIDReportType, id: HIDReportID?, timeout: Duration?) async throws -> Data](hiddeviceclient/dispatchgetreportrequest(type:id:timeout:).md)
  Send a get report request to the device over the transport.
- [func dispatchSetReportRequest(type: HIDReportType, id: HIDReportID?, data: Data, timeout: Duration?) async throws](hiddeviceclient/dispatchsetreportrequest(type:id:data:timeout:).md)
  Send a set report request to the device over the transport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/seizedevice())*