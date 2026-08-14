# CTCellularPlanStatusAvailability

**Framework**: Core Telephony  
**Kind**: enum

Constants that indicate whether the device has a cellular plan for the given phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum CTCellularPlanStatusAvailability
```

#### Overview

The [`getHintForPhoneNumber(_:completion:)`](ctcellularplanstatus/gethintforphonenumber(_:completion:).md) method returns this value alongside a [`CTCellularPlanStatusAvailabilityConfidence`](ctcellularplanstatusavailabilityconfidence.md) value in its completion handler.

## Topics

### Determining availability
- [CTCellularPlanStatusAvailability.available](ctcellularplanstatusavailability/available.md)
  A status that indicates the phone number has an active cellular plan on the device.
- [CTCellularPlanStatusAvailability.unavailable](ctcellularplanstatusavailability/unavailable.md)
  A status that indicates the phone number’s cellular plan is inactive or the system can’t determine the status.
### Creating an availability state
- [init?(rawValue: Int)](ctcellularplanstatusavailability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func getHintForPhoneNumber(String, completion: (CTCellularPlanStatusAvailability, CTCellularPlanStatusAvailabilityConfidence, (any Error)?) -> Void)](ctcellularplanstatus/gethintforphonenumber(_:completion:).md)
  Provides an estimate of the system’s confidence of the existence of an active cellular plan for the device’s phone number.
- [enum CTCellularPlanStatusAvailabilityConfidence](ctcellularplanstatusavailabilityconfidence.md)
  Constants that indicate the system’s confidence that the device has a cellular plan for a given phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusavailability)*