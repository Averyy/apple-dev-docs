# Photos Library Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app has read-write access to the user’s Photos library.

**Availability**:
- macOS 10.7+

## Details

- **Name**: `com.apple.security.personal-information.photos-library` (Photos Library)
- **Type**: boolean

#### Discussion

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode. Then, under Resource Access, select Photos Library.

## See Also

### Personal information
- [Address book entitlement](./com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](./com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](./com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.personal-information.photos-library)*