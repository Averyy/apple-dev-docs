# SRError.Code.promptDeclined

**Framework**: SensorKit  
**Kind**: case  
**Role**: Case

Occurs when the user cancels the sensor approval workflow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case promptDeclined
```

```c
SRErrorPromptDeclined
```

## Discussion

The [`requestAuthorization(sensors:completion:)`](../../srsensorreader/requestauthorization%28sensors,completion%29.md) passes this error into the completion closure if the user declines the prompt by pressing Cancel. The framework also cancels the prompt if you call this function after the user had already responded to the prompt either by approving or denying access to the argument sensors.

## See Also

### Errors
- [SRError.Code.dataInaccessible](./datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](./fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.invalidEntitlement](./invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [SRError.Code.noAuthorization](./noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined)*