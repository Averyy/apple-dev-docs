# associatedIccid

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The integrated circuit card identifier (ICCID) that identifies a SIM.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var associatedIccid: String? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) NSString * associatedIccid;
```

## See Also

### Getting the eSIM properties
- [var simCapability: CTCellularPlanCapability](./simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](./supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [CTCellularPlanProperties.lifecycle](./lifecycle.md)
  A type that contains lifecycle details for a time-limited cellular plan.
- [var lifecycleProperties: CTCellularPlanProperties.lifecycle?](./lifecycleproperties.md)
  The lifecycle details for a time-limited cellular plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/associatediccid)*