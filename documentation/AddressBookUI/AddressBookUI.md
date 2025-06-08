# Address Book UI

**Framework**: Address Book UI  
**Kind**: module

Access users’ contacts and display them in a graphical interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

#### Overview

The AddressBookUI framework provides controllers that facilitate displaying, editing, selecting, and creating records in the Address Book database.

> ❗ **Important**:  Do not use the AddressBookUI framework in iOS 9 and later. Use the APIs defined in the [`Contacts UI`](https://developer.apple.com/documentation/ContactsUI) framework instead.

## Topics

### People Picker
- [class ABPeoplePickerNavigationController](abpeoplepickernavigationcontroller.md)
  The `ABPeoplePickerNavigationController` class (whose instances are known as ) implements a view controller that manages a set of views that allow the user to select a contact or one of its contact-information items from an address book.
### Detail Display
- [class ABNewPersonViewController](abnewpersonviewcontroller.md)
  A view controller presenting an interface to create a contact.
- [class ABPersonViewController](abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as ) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as ) implements a view controller used to create a person record from a set of person properties.
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](abcreatestringwithaddressdictionary(_:_:).md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AddressBookUI)*