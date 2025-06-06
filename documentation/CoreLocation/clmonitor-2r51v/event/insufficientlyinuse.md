# insufficientlyInUse

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var insufficientlyInUse: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), then the app isn’t receiving location updates because it’s insufficiently in use.

## See Also

- [var accuracyLimited: Bool](clmonitor-2r51v/event/accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
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
- [var persistenceUnavailable: Bool](clmonitor-2r51v/event/persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [var serviceSessionRequired: Bool](clmonitor-2r51v/event/servicesessionrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/insufficientlyinuse)*