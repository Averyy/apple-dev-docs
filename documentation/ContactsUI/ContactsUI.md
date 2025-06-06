# Contacts UI

**Framework**: Contacts UI  
**Kind**: module

Provide an interface that allows people to display information about their contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+

#### Overview

The Contacts UI framework contains user interface objects that provide access to a person’s contacts in your app. Depending on your app’s authorization level for using contacts (as indicated by [`authorizationStatus(for:)`](https://developer.apple.com/documentation/Contacts/CNContactStore/authorizationStatus(for:))), your app may be able to display, edit, select, and create contacts. When the authorization level is [`CNAuthorizationStatus.limited`](https://developer.apple.com/documentation/Contacts/CNAuthorizationStatus/limited), you can display a [`ContactAccessButton`](contactaccessbutton.md) to request access to contacts beyond the limited set a person has currently granted your app access to.

## Topics

### Contact viewer
- [class CNContactViewController](cncontactviewcontroller.md)
  A view controller that displays a new, unknown, or existing contact.
### Contact pickers
- [class CNContactPickerViewController](cncontactpickerviewcontroller.md)
  A view controller that displays an interface for picking contacts.
- [class CNContactPicker](cncontactpicker.md)
  A popover-based interface for selecting a contact.
### Contact access
- [struct ContactAccessButton](contactaccessbutton.md)
  A SwiftUI button that you use to add to the set of contacts someone shares with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ContactsUI)*