# accuracyLimited

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether the app receives accuracy-limited location updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var accuracyLimited: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), then the app receives accuracy-limited location updates.

## See Also

- [var authorizationDenied: Bool](clmonitor-2r51v/event/authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [var authorizationDeniedGlobally: Bool](clmonitor-2r51v/event/authorizationdeniedglobally.md)
  A Boolean value that indicates whether the app has system-wide authorization.
- [var authorizationRequestInProgress: Bool](clmonitor-2r51v/event/authorizationrequestinprogress.md)
- [var authorizationRestricted: Bool](clmonitor-2r51v/event/authorizationrestricted.md)
  A Boolean value that indicates whether the app can make authorization changes.
- [var conditionLimitExceeded: Bool](clmonitor-2r51v/event/conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [var conditionUnsupported: Bool](clmonitor-2r51v/event/conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [var insufficientlyInUse: Bool](clmonitor-2r51v/event/insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [var persistenceUnavailable: Bool](clmonitor-2r51v/event/persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [var serviceSessionRequired: Bool](clmonitor-2r51v/event/servicesessionrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/accuracylimited)*