# SRError.Code.promptDeclined

**Framework**: SensorKit  
**Kind**: case

Occurs when the user cancels the sensor approval workflow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case promptDeclined
```

#### Discussion

The [`requestAuthorization(sensors:completion:)`](srsensorreader/requestauthorization(sensors:completion:).md) passes this error into the completion closure if the user declines the prompt by pressing Cancel. The framework also cancels the prompt if you call this function after the user had already responded to the prompt either by approving or denying access to the argument sensors.

## See Also

- [SRError.Code.dataInaccessible](srerror/code/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](srerror/code/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.invalidEntitlement](srerror/code/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [SRError.Code.noAuthorization](srerror/code/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined)*