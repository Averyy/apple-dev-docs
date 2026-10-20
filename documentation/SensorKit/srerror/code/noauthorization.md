# SRError.Code.noAuthorization

**Framework**: SensorKit  
**Kind**: case  
**Role**: Case

Occurs when the user declines sensor access in the Settings app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case noAuthorization
```

```c
SRErrorNoAuthorization
```

#### Discussion

This error code indicates the user denied access for the sensor on the in-app prompt, or by switching off authorization for the sensor in Settings.

## See Also

### Errors
- [SRError.Code.promptDeclined](./promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [SRError.Code.dataInaccessible](./datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](./fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.invalidEntitlement](./invalidentitlement.md)
  Occurs when the app lacks the required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code/noauthorization)*