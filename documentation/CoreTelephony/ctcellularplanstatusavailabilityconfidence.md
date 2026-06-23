# CTCellularPlanStatusAvailabilityConfidence

**Framework**: Core Telephony  
**Kind**: enum

Constants that indicate the system’s confidence that the device has a cellular plan for a given phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum CTCellularPlanStatusAvailabilityConfidence
```

#### Overview

The [`getHintForPhoneNumber(_:completion:)`](ctcellularplanstatus/gethintforphonenumber(_:completion:).md) method returns a value of this type in its completion handler along with the [`CTCellularPlanStatusAvailability`](ctcellularplanstatusavailability.md) determination to which it applies. Evaluate the values together when your app considers the result.

## Topics

### Determining a confidence level
- [CTCellularPlanStatusAvailabilityConfidence.high](ctcellularplanstatusavailabilityconfidence/high.md)
  A high level of confidence about the availability of a cellular plan.
- [CTCellularPlanStatusAvailabilityConfidence.low](ctcellularplanstatusavailabilityconfidence/low.md)
  A low level of confidence about the availability of a cellular plan.
### Creating a confidence level
- [init?(rawValue: Int)](ctcellularplanstatusavailabilityconfidence/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func getHintForPhoneNumber(String, completion: (CTCellularPlanStatusAvailability, CTCellularPlanStatusAvailabilityConfidence, (any Error)?) -> Void)](ctcellularplanstatus/gethintforphonenumber(_:completion:).md)
  Provides an estimate of the system’s confidence of the existence of an active cellular plan for the device’s phone number.
- [enum CTCellularPlanStatusAvailability](ctcellularplanstatusavailability.md)
  Constants that indicate whether the device has a cellular plan for the given phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusavailabilityconfidence)*