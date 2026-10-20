# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method

Returns a value indicating whether the app is authorized to gather pedometer data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- watchOS 4.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

## See Also

- [class func isStepCountingAvailable() -> Bool](cmpedometer/isstepcountingavailable.md)
  Returns a Boolean value indicating whether step counting is available on the current device.
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
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())*