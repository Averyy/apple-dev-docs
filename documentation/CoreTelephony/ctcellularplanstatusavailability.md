# CTCellularPlanStatusAvailability

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate whether the device has a cellular plan for the given phone number.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum CTCellularPlanStatusAvailability
```

```c
enum CTCellularPlanStatusAvailability : NSInteger;
```

#### Overview

The [`getHintForPhoneNumber(_:completion:)`](./ctcellularplanstatus/gethintforphonenumber%28_,completion%29.md) method returns this value alongside a [`CTCellularPlanStatusAvailabilityConfidence`](./ctcellularplanstatusavailabilityconfidence.md) value in its completion handler.

## Topics

### Determining availability
- [CTCellularPlanStatusAvailability.available](./ctcellularplanstatusavailability/available.md)
  A status that indicates the phone number has an active cellular plan on the device.
- [CTCellularPlanStatusAvailability.unavailable](./ctcellularplanstatusavailability/unavailable.md)
  A status that indicates the phone number’s cellular plan is inactive or the system can’t determine the status.
### Creating an availability state
- [init?(rawValue: Int)](./ctcellularplanstatusavailability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting a cellular plan status hint
- [class func getHintForPhoneNumber(String, completion: (CTCellularPlanStatusAvailability, CTCellularPlanStatusAvailabilityConfidence, (any Error)?) -> Void)](./ctcellularplanstatus/gethintforphonenumber%28_,completion%29.md)
  Provides an estimate of the system’s confidence of the existence of an active cellular plan for the device’s phone number.
- [enum CTCellularPlanStatusAvailabilityConfidence](./ctcellularplanstatusavailabilityconfidence.md)
  Constants that indicate the system’s confidence that the device has a cellular plan for a given phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusavailability)*