# CNAuthorizationStatus.limited

**Framework**: Contacts  
**Kind**: case

The app has access to a limited subset of contacts, chosen by the person using the app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case limited
```

## Mentions

- [Accessing the contact store](accessing-the-contact-store.md)

#### Discussion

A person can give your app limited access to their contacts by choosing this option when your app first attempts to authorize for accessing contacts. Thereafter, the person can maintain the set of contacts exposed to your app by managing them in the Settings app.

Your app can prompt the person to add contacts to the limited-access set by displaying a [`ContactAccessButton`](https://developer.apple.com/documentation/ContactsUI/ContactAccessButton), in association with a search UI your app provides. You can also display a picker to add contacts with the SwiftUI view modifier [`contactAccessPicker(isPresented:completionHandler:)`](https://developer.apple.com/documentation/SwiftUI/View/contactAccessPicker(isPresented:completionHandler:)).

## See Also

- [CNAuthorizationStatus.notDetermined](cnauthorizationstatus/notdetermined.md)
  The user has not yet made a choice regarding whether the application may access contact data.
- [CNAuthorizationStatus.restricted](cnauthorizationstatus/restricted.md)
  The application is not authorized to access contact data. The user cannot change this application’s status, possibly due to active restrictions such as parental controls being in place.
- [CNAuthorizationStatus.denied](cnauthorizationstatus/denied.md)
  The user explicitly denied access to contact data for the application.
- [CNAuthorizationStatus.authorized](cnauthorizationstatus/authorized.md)
  The application is authorized to access contact data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnauthorizationstatus/limited)*