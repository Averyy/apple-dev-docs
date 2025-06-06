# Address Book

**Framework**: Address Book  
**Kind**: module

Access the centralized database for storing users’ contacts.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+
- macOS 10.2+

#### Overview

The Address Book is a centralized database containing contacts and their personal information. Users enter personal information about themselves and their friends only once, instead of entering it repeatedly whenever the information is used. Apps that support the AddressBook framework share this contact information with other apps, including Apple’s Mail and Messages.

> ❗ **Important**:  Do not use the AddressBook framework in macOS 10.11 and later. Use the APIs defined in the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework instead.

 Do not use the AddressBook framework in macOS 10.11 and later. Use the APIs defined in the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework instead.

## Topics

### Essentials
- [class ABAddressBook](abaddressbook-swift.class.md)
  The main object you use to access the Address Book database.
### Data Types
- [class ABPerson](abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](abmultivalue-swift.class.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](abmutablemultivalue-swift.class.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](abimageclient.md)
  Methods for responding to a request to load images associated with a contact.
- [class ABRecord](abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.
### Pickers
- [class ABPeoplePickerView](abpeoplepickerview.md)
  An object you use to customize the behavior of people-picker views in an app’s user interface.
- [class ABPersonView](abpersonview.md)
  An object that provides a view for displaying and editing contacts.
### Search Elements
- [class ABSearchElement](absearchelement.md)
  An object you use to specify a search query for records in the Address Book database.
- [class ABSearchElementRef](absearchelementref.md)
  A reference to an ABSearchElement object.
### Action Plug-In
- [ABActionDelegate](abactiondelegate.md)
  Implement an Address Book action plug-in to support the display of rollover menus on top of custom items.
### C Interfaces
- [C Types](c-types.md)
  Identify the C types that correspond to Address Book objects.
- [AddressBook Functions](addressbook-functions.md)
  Find the C functions and function-like macros you use to manipulate Address Book data.
- [Address Book Constants](address-book-constants.md)
  Get the constants you use to specify Address Book information.
- [AddressBook Enumerations](addressbook-enumerations.md)
  Get the enumerations you use to specify Address Book information.
- [AddressBook Data Types](addressbook-data-types.md)
  Get the data types you use to specify Address Book information.
### Deprecated symbols
- [Deprecated symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AddressBook)*