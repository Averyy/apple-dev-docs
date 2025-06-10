# Default Record Properties

**Framework**: Address Book

Properties common to all types of records.

## Topics

### Constants
- [let kABUIDProperty: String](kabuidproperty.md)
  The unique ID for this record. It’s guaranteed never to change, no matter how much the record changes. If you need to store a reference to a record, use this value. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABCreationDateProperty: String](kabcreationdateproperty.md)
  The date when the record was first saved. Type: [`kABDateProperty`](kabdateproperty.md).
- [let kABModificationDateProperty: String](kabmodificationdateproperty.md)
  The date when the record was last saved. Type: [`kABDateProperty`](kabdateproperty.md).

## See Also

- [Address Keys](address-keys.md)
  The keys used to specify the different fields in a `kABAddressProperty`.
- [Default Person Properties](default-person-properties.md)
  The properties that a person record contains by default.
- [Default Group Properties](default-group-properties.md)
  The properties that a group record contains by default.  Developers can add their own properties with the `ABGroup` method [`addPropertiesAndTypes(_:)`](abgroup/addpropertiesandtypes(_:).md)
- [Default Multivalue List Labels](default-multivalue-list-labels.md)
  The default labels contained in the Address Book database for specifying different values in a multivalue list. Users can also add their own labels.
- [Generic Multivalue List Labels](generic-multivalue-list-labels.md)
  The generic labels contained in the Address Book database for specifying different values in a multivalue list.
- [Multivalue Property](multivalue-property.md)
  A multivalue property type.
- [Property Types](property_types.md)
  The possible [`ABPropertyType`](abpropertytype.md) types for `ABRecord` properties:


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/default-record-properties)*