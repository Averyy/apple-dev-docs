# SRError.Code.invalidEntitlement

**Framework**: SensorKit  
**Kind**: case

Occurs when the app lacks the required entitlement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case invalidEntitlement
```

#### Discussion

To allow the app to read sensor data, the system requires that the app’s code signature contain a special entitlement. For more information, see [`Configuring your project for sensor reading`](configuring-your-project-for-sensor-reading.md).

## See Also

- [SRError.Code.promptDeclined](srerror/code/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [SRError.Code.dataInaccessible](srerror/code/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](srerror/code/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.noAuthorization](srerror/code/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code/invalidentitlement)*