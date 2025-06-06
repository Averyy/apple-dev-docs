# events(for:)

**Framework**: DeviceActivity  
**Kind**: method

Fetches the events of a device activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func events(for activity: DeviceActivityName) -> [DeviceActivityEvent.Name : DeviceActivityEvent]
```

#### Return Value

The events of the activity. The dictionary is empty if your app doesn’t monitor the activity.

#### Discussion

The returned object is a static representation of the events at the time the function was called. In other words, an `Event` fetched for a particular activity doesn’t dynamically update in response to future changes made to that activity.

## Parameters

- `activity`: The name of the activity.

## See Also

- [func schedule(for: DeviceActivityName) -> DeviceActivitySchedule?](deviceactivitycenter/schedule(for:).md)
  Fetches the schedule of a device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/events(for:))*