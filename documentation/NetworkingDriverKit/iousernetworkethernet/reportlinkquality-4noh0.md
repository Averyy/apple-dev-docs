# ReportLinkQuality

**Framework**: NetworkingDriverKit  
**Kind**: method

Reports the quality of the link between the device and your driver to the system.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
IOReturn ReportLinkQuality(IOUserNetworkLinkQuality linkQuality);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Call this method to make the system aware of changes in the quality of the link between your driver and the device.

## Parameters

- `linkQuality`: The quality of the link between your driver and the device. For a list of possible values, see the constants in  .

## See Also

- [ReportLinkStatus](iousernetworkethernet/reportlinkstatus-5cxiq.md)
  Reports the status of the link between the device and your driver to the system.
- [ReportDataBandwidths](iousernetworkethernet/reportdatabandwidths-10ssx.md)
  Reports the input and output bandwidth between the device and your driver to the system.
- [IOUserNetworkLinkStatus](iousernetworklinkstatus.md)
  A type for specifying the state of your device’s connection.
- [IOUserNetworkLinkQuality](iousernetworklinkquality.md)
  A type for specifying the quality of your device’s connection to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/reportlinkquality-4noh0)*