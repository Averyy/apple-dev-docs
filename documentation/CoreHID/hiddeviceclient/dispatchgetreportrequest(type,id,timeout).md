# dispatchGetReportRequest(type:id:timeout:)

**Framework**: Core HID  
**Kind**: method  
**Role**: Instance Method

Send a get report request to the device over the transport.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func dispatchGetReportRequest(type: HIDReportType, id: HIDReportID? = nil, timeout: Duration? = nil) async throws -> Data
```

## Mentions

- [Communicating with human interface devices](../communicatingwithhiddevices.md)
- [Creating virtual devices](../creatingvirtualdevices.md)

## Return Value

The data that the device returned. Reference the device’s [`descriptor`](./descriptor.md) to determine what data the device may respond with.

## Discussion

Many HID devices respond to get report requests to retrieve information from the device. Exactly how a device responds to a get report request is dependent on the device specific implementation, but most devices conform to the reports that they declare in their report [`descriptor`](./descriptor.md). This function throws if the device is seized by another client.

For more details, see [Human Interface Devices (HID) Specifications and Tools](https://www.usb.org/hid).

> **Throws**: [`HIDDeviceError`](../hiddeviceerror.md) if there is an issue with the request.

## Parameters

- `type`: The [`HIDReportType`](../hidreporttype.md) of the requested report.
- `id`: The ID of the requested report, determined from the report descriptor. This is unnecessary if the descriptor has only one report.
- `timeout`: The maximum amount of time to wait for the device to receive the report before the call times out and fails. Not providing a duration causes the call to wait forever.

## See Also

### Interact with the device
- [func dispatchSetReportRequest(type: HIDReportType, id: HIDReportID?, data: Data, timeout: Duration?) async throws](./dispatchsetreportrequest%28type,id,data,timeout%29.md)
  Send a set report request to the device over the transport.
- [func seizeDevice() throws](./seizedevice%28%29.md)
  Attempt to obtain the device so that this client is the only active client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/dispatchgetreportrequest(type:id:timeout:))*