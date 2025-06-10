# CTCellularPlanProperties

**Framework**: Core Telephony  
**Kind**: class

An object you use for an eSIM.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class CTCellularPlanProperties
```

#### Overview

Use `CTCellularPlanProperties` to set the capabilities of your eSIMs.

## Topics

### Getting the eSIM properties
- [var associatedIccid: String?](ctcellularplanproperties/associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](ctcellularplanproperties/simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](ctcellularplanproperties/supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CTCellularPlanProvisioning](ctcellularplanprovisioning.md)
  An object you use to download and install a carrier eSIM.
- [class CTCellularPlanProvisioningRequest](ctcellularplanprovisioningrequest.md)
  A request specifying an eSIM to download and install.
- [enum CTCellularPlanCapability](ctcellularplancapability.md)
  The type of cellular plan available for an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties)*