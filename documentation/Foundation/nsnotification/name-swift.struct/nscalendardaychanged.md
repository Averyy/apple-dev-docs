# NSCalendarDayChanged

**Framework**: Foundation  
**Kind**: property

A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSCalendarDayChanged: NSNotification.Name
```

#### Discussion

If the the device is asleep when the day changes, this notification will be posted on wakeup. Only one notification will be posted on wakeup if the device has been asleep for multiple days.

There are no guarantees about the timeliness of when this notification will be received by observers. As such, you should not rely on this notification being posted or received at any precise time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nscalendardaychanged)*