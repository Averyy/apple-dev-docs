# authorizationDeniedGlobally

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app has system-wide authorization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```objc
@property (nonatomic, readonly) BOOL authorizationDeniedGlobally;
```

## Discussion

If this property is [`true`](../../Swift/true.md), then the app isn’t receiving location updates because it’s denied system-wide authorization.

## See Also

### Event states
- [accuracyLimited](./accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDenied](./authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [authorizationRequestInProgress](./authorizationrequestinprogress.md)
- [authorizationRestricted](./authorizationrestricted.md)
  A Boolean value that indicates whether the app can make authorization changes.
- [conditionLimitExceeded](./conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [conditionUnsupported](./conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [insufficientlyInUse](./insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [persistenceUnavailable](./persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](./servicesessionrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringevent/authorizationdeniedglobally)*