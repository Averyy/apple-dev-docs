# CTCellularPlanProvisioningAddPlanResult

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CTCellularPlanProvisioningAddPlanResult : NSUInteger;
```

## Topics

### Results
- [CTCellularPlanProvisioningAddPlanResult.fail](./ctcellularplanprovisioningaddplanresult/fail.md)
  The requested eSIM provisioning failed.
- [CTCellularPlanProvisioningAddPlanResult.success](./ctcellularplanprovisioningaddplanresult/success.md)
  The requested eSIM provisioning succeeded.
- [CTCellularPlanProvisioningAddPlanResult.unknown](./ctcellularplanprovisioningaddplanresult/unknown.md)
  The result of the requested eSIM provisioning is unknown.
- [CTCellularPlanProvisioningAddPlanResult.cancel](./ctcellularplanprovisioningaddplanresult/cancel.md)
### Initializers
- [init?(rawValue: UInt)](./ctcellularplanprovisioningaddplanresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Provisioning an eSIM
- [func supportsCellularPlan() -> Bool](./ctcellularplanprovisioning/supportscellularplan%28%29.md)
  Returns whether the device and your app meet eSIM provisioning requirements.
- [var supportsEmbeddedSIM: Bool](./ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./ctcellularplanprovisioning/addplan%28request,properties,completionhandler%29.md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./ctcellularplanprovisioning/addplan%28with,completionhandler%29.md)
  Starts the provisioning process for a specified eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningaddplanresult)*