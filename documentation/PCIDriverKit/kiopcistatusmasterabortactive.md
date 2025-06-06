# kIOPCIStatusMasterAbortActive

**Framework**: PCIDriverKit  
**Kind**: case

The bit that indicates whether a requester received a completion with an unsupported request completion status

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOPCIStatusMasterAbortActive
```

## See Also

- [kIOPCIStatusInterrupt](kiopcistatusinterrupt.md)
  The bit that contains the interrupt status.
- [kIOPCIStatusCapabilities](kiopcistatuscapabilities.md)
  The bit that indicates the presence of an extended capability list item.
- [kIOPCIStatusPCI66](kiopcistatuspci66.md)
  The bit that indicates the device is capable of 66 MHz operation.
- [kIOPCIStatusUDF](kiopcistatusudf.md)
  The bit that indicates the status of UDF support.
- [kIOPCIStatusFastBack2Back](kiopcistatusfastback2back.md)
  The bit that indicates whether the device is capable of fast back-to-back transactions.
- [kIOPCIStatusTargetAbortCapable](kiopcistatustargetabortcapable.md)
  The bit that indicates whether a function completed a posted or non-posted request as a completer abort error.
- [kIOPCIStatusTargetAbortActive](kiopcistatustargetabortactive.md)
  The bit that indicates whether a requester received a completion with a completer abort completion status.
- [kIOPCIStatusSERRActive](kiopcistatusserractive.md)
  The bit that indicates whether a function sent a fatal or nonfatal error message and set the SERR enable bit in the command register.
- [kIOPCIStatusParityErrActive](kiopcistatusparityerractive.md)
  The bit that indicates whether a function received a poisoned transaction-layer packet.
- [kIOPCIStatusDevSel0](kiopcistatusdevsel0.md)
  The DEVSEL timing status is set to 0.
- [kIOPCIStatusDevSel1](kiopcistatusdevsel1.md)
  The DEVSEL timing status is set to 1.
- [kIOPCIStatusDevSel2](kiopcistatusdevsel2.md)
  The DEVSEL timing status is set to 2.
- [kIOPCIStatusDevSel3](kiopcistatusdevsel3.md)
  The DEVSEL timing status is set to 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/kiopcistatusmasterabortactive)*