# fetchRequestInvalid

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

Occurs when the app misconfigures a fetch request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var fetchRequestInvalid: SRError.Code { get }
```

## See Also

### Identifying an Error Cause
- [static var promptDeclined: SRError.Code](./promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [static var dataInaccessible: SRError.Code](./datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [static var invalidEntitlement: SRError.Code](./invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [static var noAuthorization: SRError.Code](./noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)*