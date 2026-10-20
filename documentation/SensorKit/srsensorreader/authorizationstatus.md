# authorizationStatus

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The status of the user’s agreement to let the app access this reader’s sensor.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
var authorizationStatus: SRAuthorizationStatus { get }
```

```objc
@property (readonly) SRAuthorizationStatus authorizationStatus;
```

#### Discussion

When an app wishes to read data from a particular sensor, it checks for user approval first by accessing the value of this property. If the value is [`SRAuthorizationStatus.authorized`](../srauthorizationstatus/authorized.md), an app may begin recording (see [`startRecording()`](./startrecording%28%29.md)) and execute data fetches (see [`fetch(_:)`](./fetch%28_%29.md)).

If the value is [`SRAuthorizationStatus.denied`](../srauthorizationstatus/denied.md), an app can’t begin recording or execute fetches until the user switches on authorization for the reader’s sensor in Settings.

If the value is [`SRAuthorizationStatus.notDetermined`](../srauthorizationstatus/notdetermined.md), the user has not answered the in-app prompt. To display the prompt, call [`requestAuthorization(sensors:completion:)`](./requestauthorization%28sensors,completion%29.md).

## See Also

### Checking user authorization
- [class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)](./requestauthorization%28sensors,completion%29.md)
  Requests user permission to read one or more sensors.
- [enum SRAuthorizationStatus](../srauthorizationstatus.md)
  The states that model whether the user approves the app to read a particular sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)*