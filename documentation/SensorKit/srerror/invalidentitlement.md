# invalidEntitlement

**Framework**: SensorKit  
**Kind**: property

Occurs when the app lacks the required entitlement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var invalidEntitlement: SRError.Code { get }
```

#### Discussion

To allow the app to read sensor data, the system requires that the app’s code signature contain a special entitlement. For more information, see [`Configuring your project for sensor reading`](configuring-your-project-for-sensor-reading.md).

## See Also

- [static var promptDeclined: SRError.Code](srerror/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [static var dataInaccessible: SRError.Code](srerror/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [static var fetchRequestInvalid: SRError.Code](srerror/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [static var noAuthorization: SRError.Code](srerror/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement)*