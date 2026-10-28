# supportedRegionCodes

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The available regions that your eSIM supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var supportedRegionCodes: [Locale.Region] { get set }
```

## Discussion

Use 2-letter country codes as defined per [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/)

## See Also

### Getting the eSIM properties
- [var associatedIccid: String?](./associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](./simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [CTCellularPlanProperties.lifecycle](./lifecycle.md)
  A type that contains lifecycle details for a time-limited cellular plan.
- [var lifecycleProperties: CTCellularPlanProperties.lifecycle?](./lifecycleproperties.md)
  The lifecycle details for a time-limited cellular plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/supportedregioncodes-yhu5)*