# authorizationStatus

**Framework**: SensorKit  
**Kind**: property

The status of the user’s agreement to let the app access this reader’s sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var authorizationStatus: SRAuthorizationStatus { get }
```

#### Discussion

When an app wishes to read data from a particular sensor, it checks for user approval first by accessing the value of this property. If the value is [`SRAuthorizationStatus.authorized`](srauthorizationstatus/authorized.md), an app may begin recording (see [`startRecording()`](srsensorreader/startrecording().md)) and execute data fetches (see [`fetch(_:)`](srsensorreader/fetch(_:).md)).

If the value is [`SRAuthorizationStatus.denied`](srauthorizationstatus/denied.md), an app can’t begin recording or execute fetches until the user switches on authorization for the reader’s sensor in Settings.

If the value is [`SRAuthorizationStatus.notDetermined`](srauthorizationstatus/notdetermined.md), the user has not answered the in-app prompt. To display the prompt, call [`requestAuthorization(sensors:completion:)`](srsensorreader/requestauthorization(sensors:completion:).md).

## See Also

- [class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)](srsensorreader/requestauthorization(sensors:completion:).md)
  Requests user permission to read one or more sensors.
- [enum SRAuthorizationStatus](srauthorizationstatus.md)
  The states that model whether the user approves the app to read a particular sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)*