# Location entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may access location information from Location Services.

**Availability**:
- macOS 10.7+

## Details

- **Name**: `com.apple.security.personal-information.location` (Location)
- **Type**: boolean

## Discussion

To add this entitlement to your app, first enable the App Sandbox or Hardened Runtime capability in Xcode, and then select Location.

## See Also

### Personal information
- [Address book entitlement](./com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Calendars entitlement](./com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [Photos Library Entitlement](./com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.personal-information.location)*