# requestMonitorWithConfiguration:completion:

**Framework**: Core Location  
**Kind**: method  
**Role**: Type Method

Creates a location monitor with the configuration and event handler you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
+ (void) requestMonitorWithConfiguration:(CLMonitorConfiguration *) config completion:(void (^)(CLMonitor *monitor)) completionHandler;
```

#### Discussion

Configure the location monitor by adding or removing conditions for monitoring by this instance of `CLMonitor`. When an event occurs, the framework calls the block you pass in on the specified queue and delivers an instance of [`CLMonitoringEvent`](../clmonitoringevent.md). The event contains the identifier for the condition you’re monitoring, an optional instance of [`CLCondition`](../clcondition-swift.protocol.md) containing specifics, the new state, and the event’s timestamp.

All interaction directly with the returned `CLMonitor` needs to occur on the specified queue. Failing to do so results in undefined behavior.

Conditions you add to an instance of `CLMonitor` persist until you remove them from monitoring. However, Core Location stops monitoring conditions if an event is pending for them, and there isn’t a configured `CLMonitor` to receive it.

The framework stores conditions in an opaque file at `~/Library/CoreLocation/BundleId`. Alternatively, you can access the conditions in the file at `~/Library/CoreLocation/`*process name*`/name.monitor`. You can determine your app’s process name using the ActivityMonitor app or by using the UNIX `ps -al` command in Terminal.

Note that for containerized apps, this is inside the data container. Apps need to observe when protected data becomes available using [`protectedDataDidBecomeAvailableNotification`](../../UIKit/uiapplication/protecteddatadidbecomeavailablenotification.md) before creating a [`CLMonitor`](../clmonitor-2r51v.md) instance. Persistence of conditions enables an app to query efficiently for conditions it’s currently monitoring and the most recent event it delivers for each.

The app can choose to initialize the monitoring state for a condition. By default, the monitoring state is [`CLMonitoringStateUnknown`](../clmonitoringstate/clmonitoringstateunknown.md).

> **Note**:  An app can only open one instance of `CLMonitor` with a given name at a time. Attempting to open another instance with the same name returns `false`.

## Parameters

- `config`: The configuration that describes the conditions that satisfy this location monitor.
- `completionHandler`: The handler the framework calls with events that satisfy the monitor’s conditions.

## See Also

### Creating a monitor
- [CLMonitorConfiguration](../clmonitorconfiguration.md)
  An object for configuring a location monitor instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/requestmonitorwithconfiguration:completion:)*