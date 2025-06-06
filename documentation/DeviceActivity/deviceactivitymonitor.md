# DeviceActivityMonitor

**Framework**: Deviceactivity  
**Kind**: class

The object that monitors scheduled device activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@objc
class DeviceActivityMonitor
```

#### Overview

`DeviceActivityMonitor` provides the entry point into a device activity monitor extension. You should subclass `DeviceActivityMonitor` and designate your subclass as the principal class of your app extension.

The following code implements `DeviceActivityMonitor` in an app:

```swift
class MyMonitorExtension: DeviceActivityMonitor {
  let store = ManagedSettingsStore()

  // You can use the `store` property to shield apps when an interval starts, ends, or meets a threshold.
  override func intervalDidStart(for activity: DeviceActivityName) {
      super.intervalDidStart(for: activity)

      // Shield selected applications.
      let model = MyModel()
      let applications = model.selectionToShield.applications
      store.shield.applications = applications.isEmpty ? nil : applications
   }
```

> **Note**: Shielding an app dims the app’s icon on the homescreen and applies an hourglass symbol. When the app launches, the system covers it with a view that your app can configure.

## Topics

### Configuring a Monitor
- [init()](deviceactivitymonitor/init.md)
  Creates a new monitor implemented by subclasses.
### Monitoring Scheduled Intervals
- [func intervalDidEnd(for: DeviceActivityName)](deviceactivitymonitor/intervaldidend(for:).md)
  Indicates that the device activity interval ended.
- [func intervalDidStart(for: DeviceActivityName)](deviceactivitymonitor/intervaldidstart(for:).md)
  Indicates that the device activity interval started.
- [func intervalWillEndWarning(for: DeviceActivityName)](deviceactivitymonitor/intervalwillendwarning(for:).md)
  Warns your app of an ongoing activity’s conclusion a specified time before the activity ends.
- [func intervalWillStartWarning(for: DeviceActivityName)](deviceactivitymonitor/intervalwillstartwarning(for:).md)
  Warns your app of an upcoming activity a specified time before the activity starts.
### Monitoring Event Thresholds
- [func eventDidReachThreshold(DeviceActivityEvent.Name, activity: DeviceActivityName)](deviceactivitymonitor/eventdidreachthreshold(_:activity:).md)
  Indicates that the activity reached its threshold.
- [func eventWillReachThresholdWarning(DeviceActivityEvent.Name, activity: DeviceActivityName)](deviceactivitymonitor/eventwillreachthresholdwarning(_:activity:).md)
  Warns your app that an activity is about to reach its threshold.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceActivity/deviceactivitymonitor)*