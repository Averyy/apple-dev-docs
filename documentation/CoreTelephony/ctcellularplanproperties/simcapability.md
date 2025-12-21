# simCapability

**Framework**: Core Telephony  
**Kind**: property

The available type of cellular plan that your eSIM supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var simCapability: CTCellularPlanCapability { get set }
```

#### Discussion

Use to define whether your eSIM is capable of data only or data and voice. Refer to [`CTCellularPlanCapability.dataOnly`](ctcellularplancapability/dataonly.md) or [`CTCellularPlanCapability.dataAndVoice`](ctcellularplancapability/dataandvoice.md).

## See Also

- [var associatedIccid: String?](ctcellularplanproperties/associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var supportedRegionCodes: [Locale.Region]](ctcellularplanproperties/supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/simcapability)*