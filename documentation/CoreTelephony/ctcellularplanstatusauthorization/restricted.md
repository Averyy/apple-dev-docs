# CTCellularPlanStatusAuthorization.restricted

**Framework**: Core Telephony  
**Kind**: case  
**Role**: Case

A status that indicates a feature is unavailable for the given phone number.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
case restricted
```

```c
CTCellularPlanStatusAuthorizationRestricted
```

## See Also

### Determining an authorization state
- [CTCellularPlanStatusAuthorization.authorized](./authorized.md)
  A status that indicates the person granted authorization to access cellular plan status information for the phone number.
- [CTCellularPlanStatusAuthorization.notAuthorized](./notauthorized.md)
  A status that indicates the person didn’t grant authorization, or explicitly denied it.
- [CTCellularPlanStatusAuthorization.notSupported](./notsupported.md)
  A status that indicates the system can’t determine authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatusauthorization/restricted)*