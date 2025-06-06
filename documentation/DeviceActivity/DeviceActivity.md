# DeviceActivity

**Framework**: DeviceActivity  
**Kind**: module

Monitor device activity with your app extension while maintaining user privacy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

#### Overview

Device Activity provides a privacy-preserving way for an application to monitor a user’s application and website activity. For instance, you can set up a bedtime schedule that monitors device activity while the user is supposed to be asleep. Your app extension can receive warnings before an activity’s schedule starts or ends, or when an activity is about to reach a predefined threshold. You can monitor the time spent on websites and apps to warn the user once they have reached their threshold.

![A diagram depicting different kinds of device activity the framework can monitor. On the left are three icons in a vertical row, including an App store icon, a Settings icon, and a Safari icon. All three icons have arrows pointing to a clock.](https://docs-assets.developer.apple.com/published/c79b787bbcf2be82c54de00a0ec7610c/device-activity-overview%402x.png)

## Topics

### Manage Activities
- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivityName](deviceactivityname.md)
  The unique name of an activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.
### Monitor Activity
- [class DeviceActivityMonitor](deviceactivitymonitor.md)
  The object that monitors scheduled device activity.
### Errors
- [DeviceActivityCenter.MonitoringError](deviceactivitycenter/monitoringerror.md)
  Errors that may occur when starting to monitor an activity.
### Classes
- [class DeviceActivityAuthorization](deviceactivityauthorization.md)
### Protocols
- [protocol DeviceActivityAuthorizing](deviceactivityauthorizing.md)
- [protocol DeviceActivityReportExtension](deviceactivityreportextension.md)
  An app extension that reports device activity data.
- [protocol DeviceActivityReportScene](deviceactivityreportscene.md)
  Defines a custom device activity report scene.
### Structures
- [struct DeviceActivityData](deviceactivitydata.md)
  Represents the activity of a [`DeviceActivityData.User`](deviceactivitydata/user-swift.struct.md) on a particular [`DeviceActivityData.Device`](deviceactivitydata/device-swift.struct.md).
- [struct DeviceActivityFilter](deviceactivityfilter.md)
  A type that filters the device activity data to include in a report.
- [struct DeviceActivityReport](deviceactivityreport.md)
  A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.
- [struct DeviceActivityReportBuilder](deviceactivityreportbuilder.md)
  A result builder that combines one or more `DeviceActivityReportScene`s into a single scene.
- [struct DeviceActivityResults](deviceactivityresults.md)
  An asynchronous sequence of filtered device activity results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceActivity)*