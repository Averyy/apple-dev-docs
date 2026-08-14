# CTCellularPlanProvisioning

**Framework**: Core Telephony  
**Kind**: class

An object you use to download and install a carrier eSIM.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCellularPlanProvisioning
```

#### Overview

This class is only available to carrier apps with the [`com.apple.CommCenter.fine-grained`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.commcenter.fine-grained) entitlement, where the entitlement’s array of values includes `public-cellular-plan`.

## Topics

### Provisioning an eSIM
- [func supportsCellularPlan() -> Bool](ctcellularplanprovisioning/supportscellularplan.md)
  Returns whether the device and your app meet eSIM provisioning requirements.
- [var supportsEmbeddedSIM: Bool](ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](ctcellularplanprovisioning/addplan(request:properties:completionhandler:).md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](ctcellularplanprovisioning/addplan(with:completionhandler:).md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.
### Updating eSIM information
- [func update(CTCellularPlanProperties, completionHandler: ((any Error)?) -> Void)](ctcellularplanprovisioning/update(_:completionhandler:).md)
  Updates the capability and region availability for an eSIM.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CTCellularPlanProvisioningRequest](ctcellularplanprovisioningrequest.md)
  A request specifying an eSIM to download and install.
- [class CTCellularPlanProperties](ctcellularplanproperties.md)
  An object you use for an eSIM.
- [enum CTCellularPlanCapability](ctcellularplancapability.md)
  The type of cellular plan available for an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning)*