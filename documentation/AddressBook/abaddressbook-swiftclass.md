# ABAddressBook

**Framework**: Address Book  
**Kind**: class

The main object you use to access the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
class ABAddressBook
```

#### Overview

The `ABAddressBook` class provides a programming interface to the Address Book—a centralized database used by multiple applications to store contact and other personal information about people. The Address Book database also supports the notion of a “group” containing one or more persons. People may belong to multiple groups, and groups may also belong to other groups with some restrictions (for example, no circular references are allowed).

The `ABAddressBook` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABAddressBookRef` type is interchangeable in function or method calls with instances of the `ABAddressBook` class.

## Topics

### Creating and Initializing an Address Book
- [class func shared() -> ABAddressBook!](abaddressbook-swift.class/shared.md)
  Returns the unique shared instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.
### Retrieving Groups and People
- [func groups() -> [Any]!](abaddressbook-swift.class/groups.md)
  Returns an array of all the groups in the Address Book database.
- [func people() -> [Any]!](abaddressbook-swift.class/people.md)
  Returns an array of all the people in the Address Book database.
### Setting and Retrieving the Logged-in User’s Record
- [func me() -> ABPerson!](abaddressbook-swift.class/me.md)
  Returns the `ABPerson` record that represents the logged-in user.
- [func setMe(ABPerson!)](abaddressbook-swift.class/setme(_:).md)
  Sets the record that represents the logged-in user.
### Retrieving a Specific Record
- [func record(forUniqueId: String!) -> ABRecord!](abaddressbook-swift.class/record(foruniqueid:).md)
  Returns the person or group record that matches the given unique ID.
### Retrieving the Class of a Record
- [func recordClass(fromUniqueId: String!) -> String!](abaddressbook-swift.class/recordclass(fromuniqueid:).md)
  Returns the class name of the record that matches the given unique ID.
### Retrieving a Formatted Address
- [func formattedAddress(from: [AnyHashable : Any]!) -> NSAttributedString!](abaddressbook-swift.class/formattedaddress(from:).md)
  Returns an attributed string containing the formatted address.
### Retrieving Default Values
- [func defaultCountryCode() -> String!](abaddressbook-swift.class/defaultcountrycode.md)
  Returns the default country code for records with unspecified country codes.
- [func defaultNameOrdering() -> Int](abaddressbook-swift.class/defaultnameordering.md)
  Returns the default name ordering defined by the user in the Address Book application’s preferences.
### Adding and Removing Records
- [func add(ABRecord!, error: ()) throws](abaddressbook-swift.class/add(_:error:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](abaddressbook-swift.class/add(_:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](abaddressbook-swift.class/remove(_:error:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](abaddressbook-swift.class/remove(_:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
### Searching
- [func records(matching: ABSearchElement!) -> [Any]!](abaddressbook-swift.class/records(matching:).md)
  Returns an array of records that match the given search element, or returns an empty array if no records match the search element.
### Saving and Detecting Changes
- [func hasUnsavedChanges() -> Bool](abaddressbook-swift.class/hasunsavedchanges.md)
  Indicates whether an address book has changes that have not been saved to the Address Book database.
- [func save() -> Bool](abaddressbook-swift.class/save.md)
  Saves all the changes made since the last save.
- [func saveAndReturnError() throws](abaddressbook-swift.class/saveandreturnerror.md)
  Saves all the changes made since the last save.
### Constants
- [Database change notification keys](database-change-notification-keys.md)
  Keys contained by the user-info dictionary of the notifications posted by the Address Book framework.
- [Errors](1529225-errors.md)
  Errors codes returned by the Address Book Framework.
### Notifications
- [static let abDatabaseChanged: NSNotification.Name](../foundation/nsnotification/name/1458497-abdatabasechanged.md)
  Posted when this process has changed the Address Book database.
- [static let abDatabaseChangedExternally: NSNotification.Name](../foundation/nsnotification/name/1458671-abdatabasechangedexternally.md)
  Posted when a process other than the current one has changed the Address Book database.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class)*