# schedule(for:)

**Framework**: DeviceActivity  
**Kind**: method

Fetches the schedule of a device activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func schedule(for activity: DeviceActivityName) -> DeviceActivitySchedule?
```

#### Return Value

The schedule of the activity or `nil` if no such activity is currently monitored.

#### Discussion

The returned object is a static representation of the schedule at the time the function was called. In other words, a `Schedule` fetched for a particular activity doesn’t dynamically update in response to future changes made to that activity.

## Parameters

- `activity`: The name of the activity.

## See Also

- [func events(for: DeviceActivityName) -> [DeviceActivityEvent.Name : DeviceActivityEvent]](deviceactivitycenter/events(for:).md)
  Fetches the events of a device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/schedule(for:))*