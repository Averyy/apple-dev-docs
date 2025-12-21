# isStepCountingAvailable()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean value indicating whether step counting is available on the current device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
class func isStepCountingAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if step counting is available or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

## See Also

- [class func isDistanceAvailable() -> Bool](cmpedometer/isdistanceavailable.md)
  Returns a Boolean value indicating whether distance estimation is available on the current device.
- [class func isFloorCountingAvailable() -> Bool](cmpedometer/isfloorcountingavailable.md)
  Returns a Boolean value indicating whether floor counting is available on the current device.
- [class func isPaceAvailable() -> Bool](cmpedometer/ispaceavailable.md)
  Returns a Boolean value indicating whether pace information is available on the current device.
- [class func isCadenceAvailable() -> Bool](cmpedometer/iscadenceavailable.md)
  Returns a Boolean value indicating whether cadence information is available on the current device.
- [class func isPedometerEventTrackingAvailable() -> Bool](cmpedometer/ispedometereventtrackingavailable.md)
  Returns a Boolean value indicating whether pedometer events are available on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmpedometer/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to gather pedometer data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())*