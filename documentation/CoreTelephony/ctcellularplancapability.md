# CTCellularPlanCapability

**Framework**: Core Telephony  
**Kind**: enum

The type of cellular plan available for an eSIM.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 10.10+

## Declaration

```swift
enum CTCellularPlanCapability
```

## Topics

### Defining cellular data plans
- [init?(rawValue: Int)](ctcellularplancapability/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [CTCellularPlanCapability.dataAndVoice](ctcellularplancapability/dataandvoice.md)
  The cellular plan is available for data and voice.
- [CTCellularPlanCapability.dataOnly](ctcellularplancapability/dataonly.md)
  The cellular plan is available for data only.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CTCellularPlanProvisioning](ctcellularplanprovisioning.md)
  An object you use to download and install a carrier eSIM.
- [class CTCellularPlanProvisioningRequest](ctcellularplanprovisioningrequest.md)
  A request specifying an eSIM to download and install.
- [class CTCellularPlanProperties](ctcellularplanproperties.md)
  An object you use for an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplancapability)*