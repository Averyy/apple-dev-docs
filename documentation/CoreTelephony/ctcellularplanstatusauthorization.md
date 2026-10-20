# CTCellularPlanStatusAuthorization

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the authorization status for accessing cellular plan information for a phone number.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum CTCellularPlanStatusAuthorization
```

```c
enum CTCellularPlanStatusAuthorization : NSInteger;
```

#### Overview

The [`requestAuthorization(forPhoneNumber:completion:)`](./ctcellularplanstatus/requestauthorization%28forphonenumber,completion%29.md) and [`getAuthorizationStatus(forPhoneNumber:completion:)`](./ctcellularplanstatus/getauthorizationstatus%28forphonenumber,completion%29.md) methods return a value of this type in their completion handlers.

## Topics

### Determining an authorization state
- [CTCellularPlanStatusAuthorization.authorized](./ctcellularplanstatusauthorization/authorized.md)
  A status that indicates the person granted authorization to access cellular plan status information for the phone number.
- [CTCellularPlanStatusAuthorization.notAuthorized](./ctcellularplanstatusauthorization/notauthorized.md)
  A status that indicates the person didn’t grant authorization, or explicitly denied it.
- [CTCellularPlanStatusAuthorization.restricted](./ctcellularplanstatusauthorization/restricted.md)
  A status that indicates a feature is unavailable for the given phone number.
- [CTCellularPlanStatusAuthorization.notSupported](./ctcellularplanstatusauthorization/notsupported.md)
  A status that indicates the system can’t determine authorization.
### Creating an authorization state
- [init?(rawValue: Int)](./ctcellularplanstatusauthorization/init%28rawvalue%29.md)
  Initializes an authorization status.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting phone number authorization
- [class func requestAuthorization(forPhoneNumber: String, completion: (CTCellularPlanStatusAuthorization, (any Error)?) -> Void)](./ctcellularplanstatus/requestauthorization%28forphonenumber,completion%29.md)
  Presents a prompt that asks the person to allow cellular plan checks for their phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusauthorization)*