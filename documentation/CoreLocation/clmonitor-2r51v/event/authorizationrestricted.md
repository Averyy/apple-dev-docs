# authorizationRestricted

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app can make authorization changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var authorizationRestricted: Bool { get }
```

## See Also

### Event states
- [var accuracyLimited: Bool](./accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [var authorizationDenied: Bool](./authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [var authorizationDeniedGlobally: Bool](./authorizationdeniedglobally.md)
  A Boolean value that indicates whether the app has system-wide authorization.
- [var authorizationRequestInProgress: Bool](./authorizationrequestinprogress.md)
- [var conditionLimitExceeded: Bool](./conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [var conditionUnsupported: Bool](./conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [var insufficientlyInUse: Bool](./insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [var persistenceUnavailable: Bool](./persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [var serviceSessionRequired: Bool](./servicesessionrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/authorizationrestricted)*