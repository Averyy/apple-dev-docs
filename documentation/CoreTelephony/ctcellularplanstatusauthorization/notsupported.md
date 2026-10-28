# CTCellularPlanStatusAuthorization.notSupported

**Framework**: Core Telephony  
**Kind**: case  
**Role**: Case

A status that indicates the system can’t determine authorization.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
case notSupported
```

```c
CTCellularPlanStatusAuthorizationNotSupported
```

## Discussion

The framework returns this status when both of the following criteria are met:

- The given phone number doesn’t match a cellular plan on the device.
- At least one active cellular plan has a phone number the system can’t confirm.

Unlike [`CTCellularPlanStatusAuthorization.notAuthorized`](./notauthorized.md), this status doesn’t indicate that the person denied authorization; it also doesn’t identify a permanent condition. Although the status might be permanent for the given phone number, your app can call [`requestAuthorization(forPhoneNumber:completion:)`](../ctcellularplanstatus/requestauthorization%28forphonenumber,completion%29.md) again later to check, for example, if an underlying carrier-side condition changed.

## See Also

### Determining an authorization state
- [CTCellularPlanStatusAuthorization.authorized](./authorized.md)
  A status that indicates the person granted authorization to access cellular plan status information for the phone number.
- [CTCellularPlanStatusAuthorization.notAuthorized](./notauthorized.md)
  A status that indicates the person didn’t grant authorization, or explicitly denied it.
- [CTCellularPlanStatusAuthorization.restricted](./restricted.md)
  A status that indicates a feature is unavailable for the given phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusauthorization/notsupported)*