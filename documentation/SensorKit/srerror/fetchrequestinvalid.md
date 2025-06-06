# fetchRequestInvalid

**Framework**: SensorKit  
**Kind**: property

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

- [static var promptDeclined: SRError.Code](srerror/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [static var dataInaccessible: SRError.Code](srerror/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [static var invalidEntitlement: SRError.Code](srerror/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [static var noAuthorization: SRError.Code](srerror/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)*