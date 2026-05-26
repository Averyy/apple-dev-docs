# ABRecord

**Framework**: Address Book  
**Kind**: class

An abstract class that defines the common properties for all Address Book records.

**Availability**:
- macOS ?+

## Declaration

```swift
class ABRecord
```

#### Overview

`ABRecord` is an abstract superclass providing a common interface to, and defining common properties for, all Address Book records. A property is a field in the database record, such as the first or last name of a person record. ABRecord defines the types of properties supported, and basic methods for getting, setting, and removing property values.

The `ABRecord` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABRecordRef` type is interchangeable in function or method calls with instances of the `ABRecord` class.

## Topics

### Creating a Record
- [init!(addressBook: ABAddressBook!)](abrecord/init(addressbook:).md)
  Initializes a record using the given address book.
- [init!()](abrecord/init.md)
  Initializes a record using the shared address book.
### Retrieving and Setting Values
- [func removeValue(forProperty: String!) -> Bool](abrecord/removevalue(forproperty:).md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!) -> Bool](abrecord/setvalue(_:forproperty:).md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](abrecord/setvalue(_:forproperty:error:).md)
  Sets the value of a given property for a record, returning error information.
- [func value(forProperty: String!) -> Any!](abrecord/value(forproperty:).md)
  Returns the value of a given property for a record.
### Retrieving a Specific Record
- [func isReadOnly() -> Bool](abrecord/isreadonly.md)
  Returns whether a record is read-only.
### Getting Identifying Information
- [var displayName: String!](abrecord/displayname.md)
  A user-visible string representing the record.
- [var uniqueId: String!](abrecord/uniqueid.md)
  Returns the unique ID for a record.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ABGroup](abgroup.md)
- [ABPerson](abperson.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ABPerson](abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](abmultivalue.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](abmutablemultivalue.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](abimageclient.md)
  Methods for responding to a request to load images associated with a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord)*