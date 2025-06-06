# Setting an alarm

**Framework**: EventKit

Alert users of events and reminders with an alarm.

#### Overview

An easy way to alert users of their upcoming events is to give them the option of setting alarms for their calendar items. Regardless of the app that’s currently running, alarms come to the foreground as a notification and remind users of the scheduled event. If an alarm is set to a calendar event, the notification comes from the Calendar app; if an alarm is set to a reminder, the notification comes from the Reminders app.

Alarms can be time-based, firing at a specified time, or location-based, firing when crossing a geofence (for more information about geofences, see “`Configure Geofences`”). Alarms can be applied to both calendar events and reminders.

> **Note**:  An alarm is not intended to serve as a [`UILocalNotification`](https://developer.apple.com/documentation/UIKit/UILocalNotification). An alarm requires you to create an event or reminder that is visible in the user’s Calendar or Reminders app. A [`UILocalNotification`](https://developer.apple.com/documentation/UIKit/UILocalNotification) is better suited for general purposes that don’t involve the Calendar database.

 An alarm is not intended to serve as a [`UILocalNotification`](https://developer.apple.com/documentation/UIKit/UILocalNotification). An alarm requires you to create an event or reminder that is visible in the user’s Calendar or Reminders app. A [`UILocalNotification`](https://developer.apple.com/documentation/UIKit/UILocalNotification) is better suited for general purposes that don’t involve the Calendar database.

##### Add and Remove Alarms

Add an alarm to an event with the [`addAlarm(_:)`](ekcalendaritem/addalarm(_:).md) method.

Alarms can be created with an absolute date or with an offset relative to the start date of the event. Alarms created with a relative offset must occur before or at the start date of the event.

In OS X, you can trigger an action alongside the alarm. For example, you can set properties such as:

- [`emailAddress`](ekalarm/emailaddress.md) to send an email.
- [`soundName`](ekalarm/soundname.md) to play a sound.
- [`url`](ekalarm/url.md) to open a URL.

Remove an alarm from an event with the [`removeAlarm(_:)`](ekcalendaritem/removealarm(_:).md) method.

##### Configure Geofences

A geofence is a virtual border surrounding a geographic location that, when crossed, triggers an alarm for an event. You specify the latitude and longitude of the center and the radius of the geofence.

While geofence-enabled alarms can be applied to events, they are more practical for reminders. Geofences are a useful way to remind users of tasks they need to do when entering or exiting a certain region. For example, when a user leaves their workplace, an alarm can remind them to stop by the grocery store.

> **Note**:  Geofences are supported on both macOS and iOS, but they are more effective on mobile devices.

 Geofences are supported on both macOS and iOS, but they are more effective on mobile devices.

Configure a geofence for an event by creating an alarm and setting its structured location and proximity. Call the [`init(title:)`](ekstructuredlocation/init(title:).md) method to create a structured location. To set longitude and latitude coordinates, pass a [`CLLocation`](https://developer.apple.com/documentation/CoreLocation/CLLocation) to the [`geoLocation`](ekstructuredlocation/geolocation.md) property of the structured location returned. A value of `0` for the radius property will use the system’s default radius; to choose a radius of your own, specify a value in meters.

## See Also

- [class EKAlarm](ekalarm.md)
  A class that represents an alarm.
- [class EKStructuredLocation](ekstructuredlocation.md)
  `A` class that specifies a geofence to activate the alarm of a calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/setting-an-alarm)*