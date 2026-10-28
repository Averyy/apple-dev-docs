# SRError.Code.invalidEntitlement

**Framework**: SensorKit  
**Kind**: case  
**Role**: Case

Occurs when the app lacks the required entitlement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case invalidEntitlement
```

```c
SRErrorInvalidEntitlement
```

## Discussion

To allow the app to read sensor data, the system requires that the app’s code signature contain a special entitlement. For more information, see [Configuring your project for sensor reading](../../configuring-your-project-for-sensor-reading.md).

## See Also

### Errors
- [SRError.Code.promptDeclined](./promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [SRError.Code.dataInaccessible](./datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](./fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.noAuthorization](./noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code/invalidentitlement)*