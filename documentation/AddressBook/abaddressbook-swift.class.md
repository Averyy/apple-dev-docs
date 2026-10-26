# ABAddressBook

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

The main object you use to access the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
class ABAddressBook
```

```objc
@interface ABAddressBook : NSObject
```

#### Overview

The `ABAddressBook` class provides a programming interface to the Address Book—a centralized database used by multiple applications to store contact and other personal information about people. The Address Book database also supports the notion of a “group” containing one or more persons. People may belong to multiple groups, and groups may also belong to other groups with some restrictions (for example, no circular references are allowed).

The `ABAddressBook` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABAddressBookRef` type is interchangeable in function or method calls with instances of the `ABAddressBook` class.

## Topics

### Creating and Initializing an Address Book
- [class func shared() -> ABAddressBook!](./abaddressbook-swift.class/shared%28%29.md)
  Returns the unique shared instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.
- [+ addressBook](./abaddressbook-swift.class/addressbook.md)
  Returns a new instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.
### Retrieving Groups and People
- [func groups() -> [Any]!](./abaddressbook-swift.class/groups%28%29.md)
  Returns an array of all the groups in the Address Book database.
- [func people() -> [Any]!](./abaddressbook-swift.class/people%28%29.md)
  Returns an array of all the people in the Address Book database.
### Setting and Retrieving the Logged-in User’s Record
- [func me() -> ABPerson!](./abaddressbook-swift.class/me%28%29.md)
  Returns the `ABPerson` record that represents the logged-in user.
- [func setMe(ABPerson!)](./abaddressbook-swift.class/setme%28_%29.md)
  Sets the record that represents the logged-in user.
### Retrieving a Specific Record
- [func record(forUniqueId: String!) -> ABRecord!](./abaddressbook-swift.class/record%28foruniqueid%29.md)
  Returns the person or group record that matches the given unique ID.
### Retrieving the Class of a Record
- [func recordClass(fromUniqueId: String!) -> String!](./abaddressbook-swift.class/recordclass%28fromuniqueid%29.md)
  Returns the class name of the record that matches the given unique ID.
### Retrieving a Formatted Address
- [func formattedAddress(from: [AnyHashable : Any]!) -> NSAttributedString!](./abaddressbook-swift.class/formattedaddress%28from%29.md)
  Returns an attributed string containing the formatted address.
### Retrieving Default Values
- [func defaultCountryCode() -> String!](./abaddressbook-swift.class/defaultcountrycode%28%29.md)
  Returns the default country code for records with unspecified country codes.
- [func defaultNameOrdering() -> Int](./abaddressbook-swift.class/defaultnameordering%28%29.md)
  Returns the default name ordering defined by the user in the Address Book application’s preferences.
### Adding and Removing Records
- [func add(ABRecord!, error: ()) throws](./abaddressbook-swift.class/add%28_,error%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](./abaddressbook-swift.class/add%28_%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](./abaddressbook-swift.class/remove%28_,error%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](./abaddressbook-swift.class/remove%28_%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
### Searching
- [func records(matching: ABSearchElement!) -> [Any]!](./abaddressbook-swift.class/records%28matching%29.md)
  Returns an array of records that match the given search element, or returns an empty array if no records match the search element.
### Saving and Detecting Changes
- [func hasUnsavedChanges() -> Bool](./abaddressbook-swift.class/hasunsavedchanges%28%29.md)
  Indicates whether an address book has changes that have not been saved to the Address Book database.
- [func save() -> Bool](./abaddressbook-swift.class/save%28%29.md)
  Saves all the changes made since the last save.
- [func saveAndReturnError() throws](./abaddressbook-swift.class/saveandreturnerror%28%29.md)
  Saves all the changes made since the last save.
### Constants
- [Database change notification keys](./database-change-notification-keys.md)
  Keys contained by the user-info dictionary of the notifications posted by the Address Book framework.
- [Errors](./api-1529225-errors.md)
  Errors codes returned by the Address Book Framework.
### Notifications
- [static let abDatabaseChanged: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/abdatabasechanged.md)
  Posted when this process has changed the Address Book database.
- [static let abDatabaseChangedExternally: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/abdatabasechangedexternally.md)
  Posted when a process other than the current one has changed the Address Book database.
- [kABDatabaseChangedNotification](./kabdatabasechangednotification.md)
  Posted when this process has changed the Address Book database.
- [kABDatabaseChangedExternallyNotification](./kabdatabasechangedexternallynotification.md)
  Posted when a process other than the current one has changed the Address Book database.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class)*