# CTCellularPlanStatusAuthorization

**Framework**: Core Telephony  
**Kind**: enum

Constants that indicate the authorization status for accessing cellular plan information for a phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum CTCellularPlanStatusAuthorization
```

#### Overview

The [`requestAuthorization(forPhoneNumber:completion:)`](ctcellularplanstatus/requestauthorization(forphonenumber:completion:).md) and [`getAuthorizationStatus(forPhoneNumber:completion:)`](ctcellularplanstatus/getauthorizationstatus(forphonenumber:completion:).md) methods return a value of this type in their completion handlers.

## Topics

### Determining an authorization state
- [CTCellularPlanStatusAuthorization.authorized](ctcellularplanstatusauthorization/authorized.md)
  A status that indicates the person granted authorization to access cellular plan status information for the phone number.
- [CTCellularPlanStatusAuthorization.notAuthorized](ctcellularplanstatusauthorization/notauthorized.md)
  A status that indicates the person didn’t grant authorization, or explicitly denied it.
- [CTCellularPlanStatusAuthorization.restricted](ctcellularplanstatusauthorization/restricted.md)
  A status that indicates a feature is unavailable for the given phone number.
- [CTCellularPlanStatusAuthorization.notSupported](ctcellularplanstatusauthorization/notsupported.md)
  A status that indicates the system can’t determine authorization.
### Creating an authorization state
- [init?(rawValue: Int)](ctcellularplanstatusauthorization/init(rawvalue:).md)
  Initializes an authorization status.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func requestAuthorization(forPhoneNumber: String, completion: (CTCellularPlanStatusAuthorization, (any Error)?) -> Void)](ctcellularplanstatus/requestauthorization(forphonenumber:completion:).md)
  Presents a prompt that asks the person to allow cellular plan checks for their phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusauthorization)*