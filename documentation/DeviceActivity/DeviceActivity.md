# Device Activity

**Framework**: Device Activity  
**Kind**: module

Monitor device activity with your app extension while maintaining privacy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

#### Overview

Device Activity provides a privacy-preserving way for an application to monitor a person’s application and website activity. For instance, you can set up a bedtime schedule that monitors device activity while the person is supposed to be asleep. Your app extension can receive warnings before an activity’s schedule starts or ends, or when an activity is about to reach a predefined threshold. You can monitor the time spent on websites and apps to warn the person once they have reached their threshold.

![A diagram depicting different kinds of device activity the framework can monitor. On the left are three icons in a vertical row, including an App store icon, a Settings icon, and a Safari icon. All three icons have arrows pointing to a clock.](/images/com.apple.DeviceActivity/device-activity-overview@2x.png)

## Topics

### Manage activities
- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivityName](deviceactivityname.md)
  The unique name of an activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.
### Monitor activity
- [class DeviceActivityMonitor](deviceactivitymonitor.md)
  The object that monitors scheduled device activity.
### Report activity
- [struct DeviceActivityReport](deviceactivityreport.md)
  A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.
- [protocol DeviceActivityReportExtension](deviceactivityreportextension.md)
  An app extension that reports device activity data.
- [protocol DeviceActivityReportScene](deviceactivityreportscene.md)
  Defines a custom device activity report scene.
- [struct DeviceActivityReportBuilder](deviceactivityreportbuilder.md)
  A result builder that combines one or more `DeviceActivityReportScene`s into a single scene.
### Filter activity data
- [struct DeviceActivityFilter](deviceactivityfilter.md)
  A type that filters the device activity data to include in a report.
- [struct DeviceActivityData](deviceactivitydata.md)
  Activity data for a person on a specific device.
- [struct DeviceActivityResults](deviceactivityresults.md)
  An asynchronous sequence of filtered device activity results.
### Authorize access
- [class DeviceActivityAuthorization](deviceactivityauthorization.md)
- [protocol DeviceActivityAuthorizing](deviceactivityauthorizing.md)
### Handle errors
- [DeviceActivityCenter.MonitoringError](deviceactivitycenter/monitoringerror.md)
  Errors that may occur when starting to monitor an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceActivity)*