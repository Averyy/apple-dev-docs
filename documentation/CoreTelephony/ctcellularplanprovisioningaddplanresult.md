# CTCellularPlanProvisioningAddPlanResult

**Framework**: Core Telephony  
**Kind**: enum

The result from attempting to provision an eSIM.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
enum CTCellularPlanProvisioningAddPlanResult
```

## Topics

### Results
- [CTCellularPlanProvisioningAddPlanResult.fail](ctcellularplanprovisioningaddplanresult/fail.md)
  The requested eSIM provisioning failed.
- [CTCellularPlanProvisioningAddPlanResult.success](ctcellularplanprovisioningaddplanresult/success.md)
  The requested eSIM provisioning succeeded.
- [CTCellularPlanProvisioningAddPlanResult.unknown](ctcellularplanprovisioningaddplanresult/unknown.md)
  The result of the requested eSIM provisioning is unknown.
- [CTCellularPlanProvisioningAddPlanResult.cancel](ctcellularplanprovisioningaddplanresult/cancel.md)
### Initializers
- [init?(rawValue: UInt)](ctcellularplanprovisioningaddplanresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func supportsCellularPlan() -> Bool](ctcellularplanprovisioning/supportscellularplan.md)
  Indicates whether the device supports eSIM and the activation policy allows eSIM installation.
- [var supportsEmbeddedSIM: Bool](ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](ctcellularplanprovisioning/addplan(with:completionhandler:).md)
  Starts the provisioning process for a specified eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningaddplanresult)*