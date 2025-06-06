# supportsCellularPlan()

**Framework**: Core Telephony  
**Kind**: method

Indicates whether the device supports eSIM and the activation policy allows eSIM installation.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func supportsCellularPlan() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device supports eSIM and the activation policy allows eSIM installation; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method checks that the device supports eSIM installation and verifies activation policies.

It doesn’t check whether the user has installed an eSIM. You can call this method at any time.

## See Also

- [var supportsEmbeddedSIM: Bool](ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](ctcellularplanprovisioning/addplan(with:completionhandler:).md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/supportscellularplan())*