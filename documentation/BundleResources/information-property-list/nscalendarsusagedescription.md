# NSCalendarsUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to their calendar data.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- watchOS 6.0+ - Deprecated in 10.0

> **Deprecated**: `NSCalendarsUsageDescription` has been deprecated. If your app needs read and write access to a person’s calendar data, use [`NSCalendarsFullAccessUsageDescription`](./nscalendarsfullaccessusagedescription.md) instead. If your app needs to create events in a person’s default calendar, use [`NSCalendarsWriteOnlyAccessUsageDescription`](./nscalendarswriteonlyaccessusagedescription.md) instead.

## Details

- **Name**: `NSCalendarsUsageDescription` (Privacy - Calendars Usage Description)
- **Type**: string

#### Discussion

> ❗ **Important**:  This key is required if your app uses APIs that access the person’s calendar data.

## See Also

### Deprecated keys
- [NSEnterpriseMCAMUsageDescription](./nsenterprisemcamusagedescription.md)
  A message that tells people why the app is requesting access to the device’s main camera.
- [NSRemindersUsageDescription](./nsremindersusagedescription.md)
  A message that tells people why the app is requesting access to their reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsusagedescription)*