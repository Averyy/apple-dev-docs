# supportsEmbeddedSIM

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device has hardware eSIM support.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var supportsEmbeddedSIM: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsEmbeddedSIM;
```

## See Also

### Provisioning an eSIM
- [func supportsCellularPlan() -> Bool](./supportscellularplan%28%29.md)
  Returns whether the device and your app meet eSIM provisioning requirements.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./addplan%28request,properties,completionhandler%29.md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./addplan%28with,completionhandler%29.md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](../ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/supportsembeddedsim)*