# Address book entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.

**Availability**:
- macOS 10.7+

#### Discussion

To add this entitlement to your app, enable the App Sandbox capability in Xcode and then select Contacts, or enable the Hardened Runtime capability and then select Address Book.

## See Also

- [Location entitlement](entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [Photos Library Entitlement](entitlements/com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.personal-information.addressbook)*