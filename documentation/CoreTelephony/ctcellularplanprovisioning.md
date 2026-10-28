# CTCellularPlanProvisioning

**Framework**: Core Telephony  
**Kind**: class  
**Role**: Class

An object you use to download and install a carrier eSIM.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCellularPlanProvisioning
```

```objc
@interface CTCellularPlanProvisioning : NSObject
```

## Overview

This class is only available to carrier apps with the [`com.apple.CommCenter.fine-grained`](../BundleResources/entitlements/com.apple.commcenter.fine-grained.md) entitlement, where the entitlement’s array of values includes `public-cellular-plan`.

## Topics

### Provisioning an eSIM
- [func supportsCellularPlan() -> Bool](./ctcellularplanprovisioning/supportscellularplan%28%29.md)
  Returns whether the device and your app meet eSIM provisioning requirements.
- [var supportsEmbeddedSIM: Bool](./ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./ctcellularplanprovisioning/addplan%28request,properties,completionhandler%29.md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./ctcellularplanprovisioning/addplan%28with,completionhandler%29.md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](./ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.
### Updating eSIM information
- [func update(CTCellularPlanProperties, completionHandler: ((any Error)?) -> Void)](./ctcellularplanprovisioning/update%28_,completionhandler%29.md)
  Updates the capability and region availability for an eSIM.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### eSIM
- [class CTCellularPlanProvisioningRequest](./ctcellularplanprovisioningrequest.md)
  A request specifying an eSIM to download and install.
- [class CTCellularPlanProperties](./ctcellularplanproperties.md)
  An object you use for an eSIM.
- [enum CTCellularPlanCapability](./ctcellularplancapability.md)
  The type of cellular plan available for an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning)*