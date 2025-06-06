# ReportDataBandwidths

**Framework**: NetworkingDriverKit  
**Kind**: method

Reports the input and output bandwidth between the device and your driver to the system.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t ReportDataBandwidths(uint64_t maxInputBandwidth, uint64_t maxOutputBandwidth, uint64_t effectiveInputBandwidth, uint64_t effectiveOutputBandwidth);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `maxInputBandwidth`: The maximum theoretical data rate for receiving data with the current medium, in bits per second.
- `maxOutputBandwidth`: The maximum theoretical data rate for sending data with the current medium, in bits per second.
- `effectiveInputBandwidth`: The effective input bandwidth, in bits per second. If you specify  , the system sets the effective bandwidth to the same value in  .
- `effectiveOutputBandwidth`: The effective output bandwidth, in bits per second. If you specify  , the system sets the effective bandwidth to the same value in  .

## See Also

- [ReportLinkStatus](iousernetworkethernet/reportlinkstatus-5cxiq.md)
  Reports the status of the link between the device and your driver to the system.
- [ReportLinkQuality](iousernetworkethernet/reportlinkquality-4noh0.md)
  Reports the quality of the link between the device and your driver to the system.
- [IOUserNetworkLinkStatus](iousernetworklinkstatus.md)
  A type for specifying the state of your device’s connection.
- [IOUserNetworkLinkQuality](iousernetworklinkquality.md)
  A type for specifying the quality of your device’s connection to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/reportdatabandwidths-10ssx)*