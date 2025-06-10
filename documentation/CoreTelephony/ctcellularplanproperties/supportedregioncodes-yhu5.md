# supportedRegionCodes

**Framework**: Core Telephony  
**Kind**: property

The available regions that your eSIM supports.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var supportedRegionCodes: [Locale.Region] { get set }
```

#### Discussion

Use 2-letter country codes as defined per [`ISO 3166-1 alpha-2`](https://developer.apple.comhttps://www.iso.org/obp/ui/#search/code/)

## See Also

- [var associatedIccid: String?](ctcellularplanproperties/associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](ctcellularplanproperties/simcapability.md)
  The available type of cellular plan that your eSIM supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/supportedregioncodes-yhu5)*