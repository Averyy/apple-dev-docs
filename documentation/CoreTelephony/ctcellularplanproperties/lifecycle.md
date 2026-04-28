# CTCellularPlanProperties.lifecycle

**Framework**: Core Telephony  
**Kind**: class

A type that contains lifecycle details for a time-limited cellular plan.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class lifecycle
```

#### Overview

This type contains lifecycle details for a time-limited cellular plan, including information such as when the plan expires. The expiration date determines the installation experience and when the system deactivates the plan.

## Topics

### Specifying the expiration date
- [var expirationDate: DateComponents](ctcellularplanproperties/lifecycle/expirationdate.md)
  The date when the time-limited cellular plan expires, specified with day-level granularity.
### Initializers
- [init?(coder: NSCoder)](ctcellularplanproperties/lifecycle/init(coder:).md)

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

- [var associatedIccid: String?](ctcellularplanproperties/associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](ctcellularplanproperties/simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](ctcellularplanproperties/supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [var lifecycleProperties: CTCellularPlanProperties.lifecycle?](ctcellularplanproperties/lifecycleproperties.md)
  The lifecycle details for a time-limited cellular plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/lifecycle)*