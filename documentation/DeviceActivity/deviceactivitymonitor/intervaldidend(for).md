# intervalDidEnd(for:)

**Framework**: Device Activity  
**Kind**: method  
**Role**: Instance Method

Indicates that the device activity interval ended.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func intervalDidEnd(for activity: DeviceActivityName)
```

#### Discussion

An activity ends when someone first uses the device outside the activity’s scheduled time interval or when your app stops monitoring an activity with an ongoing interval. In other words, the system only invokes this method when the device is in use.

## Parameters

- `activity`: The name of the activity.

## See Also

### Monitoring Scheduled Intervals
- [func intervalDidStart(for: DeviceActivityName)](./intervaldidstart%28for%29.md)
  Indicates that the device activity interval started.
- [func intervalWillEndWarning(for: DeviceActivityName)](./intervalwillendwarning%28for%29.md)
  Warns your app of an ongoing activity’s conclusion a specified time before the activity ends.
- [func intervalWillStartWarning(for: DeviceActivityName)](./intervalwillstartwarning%28for%29.md)
  Warns your app of an upcoming activity a specified time before the activity starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor/intervaldidend(for:))*