# lifecycleProperties

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The lifecycle details for a time-limited cellular plan.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var lifecycleProperties: CTCellularPlanProperties.lifecycle? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) CTCellularPlanLifecycleProperties * lifecycleProperties;
```

#### Overview

Use this property to specify lifecycle details for a time-limited cellular plan. When this property is present, the system treats the cellular plan as a temporary eSIM. Set this property to `nil` if the cellular plan doesn’t have an associated expiration date.

## See Also

### Getting the eSIM properties
- [var associatedIccid: String?](./associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](./simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](./supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [CTCellularPlanProperties.lifecycle](./lifecycle.md)
  A type that contains lifecycle details for a time-limited cellular plan.
- [supportedRegionCodes](./supportedregioncodes-5elox.md)
  The available regions that your eSIM supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/lifecycleproperties)*