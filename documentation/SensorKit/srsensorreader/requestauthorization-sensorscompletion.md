# requestAuthorization(sensors:completion:)

**Framework**: SensorKit  
**Kind**: method

Requests user permission to read one or more sensors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class func requestAuthorization(sensors: Set<SRSensor>) async throws
```

#### Discussion

> **Note**:  In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func requestAuthorization(sensors: Set<SRSensor>) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func requestAuthorization(sensors: Set<SRSensor>) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Call this function for sensors in which [`authorizationStatus`](srsensorreader/authorizationstatus.md) is [`SRAuthorizationStatus.notDetermined`](srauthorizationstatus/notdetermined.md) to display a prompt that requests user authorization. When the prompt dismisses, the framework calls the `completion` closure. Your delegate needs to wait for a call to [`sensorReader(_:didChange:)`](srsensorreaderdelegate/sensorreader(_:didchange:).md) to determine whether the user approves sensor access.

If you pass a sensor into this function for which the user already answered the in-app prompt, the framework cancels the prompt with [`SRError.Code.promptDeclined`](srerror/code/promptdeclined.md). When the user has already answered the prompt for a particular sensor, its [`authorizationStatus`](srsensorreader/authorizationstatus.md) is [`SRAuthorizationStatus.authorized`](srauthorizationstatus/authorized.md) or [`SRAuthorizationStatus.denied`](srauthorizationstatus/denied.md). The user may change the authorization status for a sensor in Settings > Privacy > Research Sensor & Usage Data.

For more information about the authorization workflow, see [`Configuring your project for sensor reading`](configuring-your-project-for-sensor-reading.md).

## Parameters

- `sensors`: One or more sensors your app requests.
- `completion`: A closure to run after the framework determines user authorization.

## See Also

- [var authorizationStatus: SRAuthorizationStatus](srsensorreader/authorizationstatus.md)
  The status of the user’s agreement to let the app access this reader’s sensor.
- [enum SRAuthorizationStatus](srauthorizationstatus.md)
  The states that model whether the user approves the app to read a particular sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))*