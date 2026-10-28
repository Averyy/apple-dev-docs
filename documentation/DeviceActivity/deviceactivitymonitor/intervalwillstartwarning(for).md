# intervalWillStartWarning(for:)

**Framework**: Device Activity  
**Kind**: method  
**Role**: Instance Method

Warns your app of an upcoming activity a specified time before the activity starts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func intervalWillStartWarning(for activity: DeviceActivityName)
```

## Discussion

When an activity is about to start, `intervalWillStartWarning` warns your app extension of the upcoming activity.

## Parameters

- `activity`: The name of the activity.

## See Also

### Monitoring Scheduled Intervals
- [func intervalDidEnd(for: DeviceActivityName)](./intervaldidend%28for%29.md)
  Indicates that the device activity interval ended.
- [func intervalDidStart(for: DeviceActivityName)](./intervaldidstart%28for%29.md)
  Indicates that the device activity interval started.
- [func intervalWillEndWarning(for: DeviceActivityName)](./intervalwillendwarning%28for%29.md)
  Warns your app of an ongoing activity’s conclusion a specified time before the activity ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor/intervalwillstartwarning(for:))*