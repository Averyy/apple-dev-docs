# noAuthorization

**Framework**: SensorKit  
**Kind**: property

Occurs when the user declines sensor access in the Settings app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var noAuthorization: SRError.Code { get }
```

## See Also

- [static var promptDeclined: SRError.Code](srerror/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [static var dataInaccessible: SRError.Code](srerror/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [static var fetchRequestInvalid: SRError.Code](srerror/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [static var invalidEntitlement: SRError.Code](srerror/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization)*