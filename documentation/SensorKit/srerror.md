# SRError

**Framework**: SensorKit  
**Kind**: struct

An error that SensorKit reports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct SRError
```

## Topics

### Inspecting Error Information
- [static var errorDomain: String](srerror/errordomain.md)
### Identifying an Error Cause
- [static var promptDeclined: SRError.Code](srerror/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [static var dataInaccessible: SRError.Code](srerror/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [static var fetchRequestInvalid: SRError.Code](srerror/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [static var invalidEntitlement: SRError.Code](srerror/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [static var noAuthorization: SRError.Code](srerror/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SRErrorDomain: String](srerrordomain.md)
  An error domain that’s unique to the framework.
- [SRError.Code](srerror/code.md)
  The kinds of problems that stop a recording or a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror)*