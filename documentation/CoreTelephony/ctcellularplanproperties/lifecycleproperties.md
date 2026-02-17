# lifecycleProperties

**Framework**: Core Telephony  
**Kind**: property

The lifecycle details for a time-limited cellular plan.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
var lifecycleProperties: CTCellularPlanProperties.lifecycle? { get set }
```

#### Overview

Use this property to specify lifecycle details for a time-limited cellular plan. When this property is present, the system treats the cellular plan as a temporary eSIM. Set this property to `nil` if the cellular plan doesn’t have an associated expiration date.

## See Also

- [var associatedIccid: String?](ctcellularplanproperties/associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](ctcellularplanproperties/simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](ctcellularplanproperties/supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [CTCellularPlanProperties.lifecycle](ctcellularplanproperties/lifecycle.md)
  A type that contains lifecycle details for a time-limited cellular plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/lifecycleproperties)*