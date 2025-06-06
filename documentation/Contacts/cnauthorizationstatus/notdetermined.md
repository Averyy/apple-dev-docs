# CNAuthorizationStatus.notDetermined

**Framework**: Contacts  
**Kind**: case

The user has not yet made a choice regarding whether the application may access contact data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case notDetermined
```

## Mentions

- [Accessing the contact store](accessing-the-contact-store.md)

## See Also

- [CNAuthorizationStatus.restricted](cnauthorizationstatus/restricted.md)
  The application is not authorized to access contact data. The user cannot change this application’s status, possibly due to active restrictions such as parental controls being in place.
- [CNAuthorizationStatus.denied](cnauthorizationstatus/denied.md)
  The user explicitly denied access to contact data for the application.
- [CNAuthorizationStatus.authorized](cnauthorizationstatus/authorized.md)
  The application is authorized to access contact data.
- [CNAuthorizationStatus.limited](cnauthorizationstatus/limited.md)
  The app has access to a limited subset of contacts, chosen by the person using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnauthorizationstatus/notdetermined)*