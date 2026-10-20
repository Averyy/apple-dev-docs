# ABRecord

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

An abstract class that defines the common properties for all Address Book records.

**Availability**:
- macOS

## Declaration

```swift
class ABRecord
```

```objc
@interface ABRecord : NSObject
```

#### Overview

`ABRecord` is an abstract superclass providing a common interface to, and defining common properties for, all Address Book records. A property is a field in the database record, such as the first or last name of a person record. ABRecord defines the types of properties supported, and basic methods for getting, setting, and removing property values.

The `ABRecord` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABRecordRef` type is interchangeable in function or method calls with instances of the `ABRecord` class.

## Topics

### Creating a Record
- [init!(addressBook: ABAddressBook!)](./abrecord-swift.class/init%28addressbook%29.md)
  Initializes a record using the given address book.
- [init!()](./abrecord-swift.class/init%28%29.md)
  Initializes a record using the shared address book.
### Retrieving and Setting Values
- [func removeValue(forProperty: String!) -> Bool](./abrecord-swift.class/removevalue%28forproperty%29.md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!) -> Bool](./abrecord-swift.class/setvalue%28_,forproperty%29.md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](./abrecord-swift.class/setvalue%28_,forproperty,error%29.md)
  Sets the value of a given property for a record, returning error information.
- [func value(forProperty: String!) -> Any!](./abrecord-swift.class/value%28forproperty%29.md)
  Returns the value of a given property for a record.
### Retrieving a Specific Record
- [func isReadOnly() -> Bool](./abrecord-swift.class/isreadonly%28%29.md)
  Returns whether a record is read-only.
### Getting Identifying Information
- [var displayName: String!](./abrecord-swift.class/displayname.md)
  A user-visible string representing the record.
- [var uniqueId: String!](./abrecord-swift.class/uniqueid.md)
  Returns the unique ID for a record.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ABGroup](./abgroup.md)
- [ABPerson](./abperson.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data Types
- [class ABPerson](./abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](./abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](./abmultivalue-swift.class.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](./abmutablemultivalue-swift.class.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](./abimageclient.md)
  Methods for responding to a request to load images associated with a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class)*