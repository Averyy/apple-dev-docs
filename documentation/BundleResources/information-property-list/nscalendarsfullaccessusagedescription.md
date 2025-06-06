# NSCalendarsFullAccessUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is requesting access to read and write their calendar data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

#### Discussion

If your app needs to create calendar events but doesn’t need to read them, use [`NSCalendarsWriteOnlyAccessUsageDescription`](information-property-list/nscalendarswriteonlyaccessusagedescription.md). If your app runs on iOS 17 or later and presents an [`EKEventEditViewController`](https://developer.apple.com/documentation/EventKitUI/EKEventEditViewController) to allow people to create calendar events, you don’t need to request calendar access.

> ❗ **Important**:  This key is required if your app uses APIs that read and write the person’s calendar data.

 This key is required if your app uses APIs that read and write the person’s calendar data.

## See Also

- [NSCalendarsWriteOnlyAccessUsageDescription](information-property-list/nscalendarswriteonlyaccessusagedescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](information-property-list/nsremindersfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.
- [Accessing the event store](../EventKit/accessing-the-event-store.md)
  Request access to a person’s calendar data through the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsfullaccessusagedescription)*