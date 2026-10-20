# NSEnterpriseMCAMUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to the device’s main camera.

**Availability**:
- visionOS 2.0+ - Deprecated in 2.3

> **Deprecated**: Use [`NSMainCameraUsageDescription`](./nsmaincamerausagedescription.md) instead.

## Details

- **Name**: `NSEnterpriseMCAMUsageDescription` (Main Camera Usage Description)
- **Type**: string

#### Discussion

The system uses this string in visionOS 2-2.3 to tell someone why your app requests permission to use the main camera. In newer versions of visionOS, the system uses the value of [`NSMainCameraUsageDescription`](./nsmaincamerausagedescription.md) instead.

For information about using the main camera in your visionOS app, see [Accessing the main camera](../../visionOS/accessing-the-main-camera.md).

## See Also

### Deprecated keys
- [NSCalendarsUsageDescription](./nscalendarsusagedescription.md)
  A message that tells people why the app is requesting access to their calendar data.
- [NSRemindersUsageDescription](./nsremindersusagedescription.md)
  A message that tells people why the app is requesting access to their reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsenterprisemcamusagedescription)*