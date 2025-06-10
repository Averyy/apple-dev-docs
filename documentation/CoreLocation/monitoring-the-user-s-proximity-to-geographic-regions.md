# Monitoring the user’s proximity to geographic regions

**Framework**: Core Location

Use condition monitoring to determine when the user enters or leaves a geographic region.

#### Overview

Condition monitoring (also known as geofencing) is a way for your app to be alerted when the user enters or exits a geographical region. You might use region monitoring to perform location-related tasks. For example, the Reminders app uses them to trigger reminders when the user arrives at or leaves a specified location, as shown in [`Figure 1`](monitoring_the_user_s_proximity_to_geographic_regions#2904074.md).

![A notification that can appear when the user leaves a geographic region](https://docs-assets.developer.apple.com/published/c95a6c5a40e05cc8815ffa7c38f2618e/media-2904074%402x.png)

In iOS, the system monitors regions and wakes up your app as needed when conditions change between satisfied and unsatisfied states. In macOS, condition monitoring works only while the app is running (either in the foreground or background) and the user’s system is awake. The system doesn’t launch Mac apps to deliver region-related notifications.

##### Define and Monitor a Geographic Condition

Define a circular area centered on a geographic coordinate using a [`CLCircularGeographicCondition`](clcirculargeographiccondition.md). The radius of the condition defines its boundary. You define the conditions you want to monitor and register them with the system by calling the [`startMonitoring(for:)`](cllocationmanager/startmonitoring(for:).md) method of your [`CLLocationManager`](cllocationmanager.md) object. The system monitors your conditions until you explicitly ask it to stop or until the device reboots.

Listing 1 shows how to configure and register a condition centered around a point provided by the caller of the method. The task uses a radius of 200 meters to define the boundaries of the condition, then awaits as [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) events arrive asynchronously from Core Location.

Listing 1. Monitoring a region around the specified coordinate

```swift
Task {    
     // Create a custom monitor.
     let monitor = await CLMonitor("my_custom_monitor")
     // Register the condition for 200 meters.
     let center = myFirstLocation;
     let condition = CLCircularGeographicCondition(center: center1, radius: 200)
     // Add the condition to the monitor.
     monitor.add(condition, identifier: "stay_within_200_meters")
     // Start monitoring.
     for try await event in monitor.events {
         // Respond to events.
         if event.state == .satisfied {
             // Process the 200 meter condition.
         }
     }
}
```

> 💡 **Tip**:  Conditions are shared resources that rely on specific hardware capabilities. To ensure that all apps can participate in condition monitoring, Core Location prevents any single app from monitoring more than 20 conditions of any type simultaneously. Prioritize what you want to monitor to based on this restriction.

If an iOS app isn’t running when a condition is satisfied, the system tries to launch it. When the app relaunches, recreate the monitor with the same identifier. Note that monitoring can only occur after the user unlocks the device after a reboot.

##### Respond to Events

Whenever the state of your app’s condition changes, Core Location provides an event through the monitor’s [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence).

If an iOS app isn’t running when a condition is satisfied, the system tries to launch it. When your app relaunches, it’s your responsibility to recreate the monitor with the same identifier. Monitoring can only occur after the user unlocks the device after a reboot.

It’s important to keep iterating events in order to determine when conditions change.

## See Also

- [class CLRegion](clregion.md)
  A base class representing an area that can be monitored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/monitoring-the-user-s-proximity-to-geographic-regions)*