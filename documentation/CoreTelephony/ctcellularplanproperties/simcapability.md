# simCapability

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The available type of cellular plan that your eSIM supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var simCapability: CTCellularPlanCapability { get set }
```

```objc
@property (nonatomic, readwrite) CTCellularPlanCapability simCapability;
```

## Discussion

Use to define whether your eSIM is capable of data only or data and voice. Refer to [`CTCellularPlanCapability.dataOnly`](../ctcellularplancapability/dataonly.md) or [`CTCellularPlanCapability.dataAndVoice`](../ctcellularplancapability/dataandvoice.md).

## See Also

### Getting the eSIM properties
- [var associatedIccid: String?](./associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var supportedRegionCodes: [Locale.Region]](./supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [CTCellularPlanProperties.lifecycle](./lifecycle.md)
  A type that contains lifecycle details for a time-limited cellular plan.
- [var lifecycleProperties: CTCellularPlanProperties.lifecycle?](./lifecycleproperties.md)
  The lifecycle details for a time-limited cellular plan.
- [supportedRegionCodes](./supportedregioncodes-5elox.md)
  The available regions that your eSIM supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/simcapability)*