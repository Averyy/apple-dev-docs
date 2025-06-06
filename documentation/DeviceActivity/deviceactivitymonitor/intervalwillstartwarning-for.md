# intervalWillStartWarning(for:)

**Framework**: DeviceActivity  
**Kind**: method

Warns your app of an upcoming activity a specified time before the activity starts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func intervalWillStartWarning(for activity: DeviceActivityName)
```

#### Discussion

When an activity is about to start, `intervalWillStartWarning` warns your app extension of the upcoming activity.

## Parameters

- `activity`: The name of the activity.

## See Also

- [func intervalDidEnd(for: DeviceActivityName)](deviceactivitymonitor/intervaldidend(for:).md)
  Indicates that the device activity interval ended.
- [func intervalDidStart(for: DeviceActivityName)](deviceactivitymonitor/intervaldidstart(for:).md)
  Indicates that the device activity interval started.
- [func intervalWillEndWarning(for: DeviceActivityName)](deviceactivitymonitor/intervalwillendwarning(for:).md)
  Warns your app of an ongoing activity’s conclusion a specified time before the activity ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor/intervalwillstartwarning(for:))*