# Generic Multivalue List Labels

**Framework**: Address Book

The generic labels contained in the Address Book database for specifying different values in a multivalue list.

#### Overview

These labels are especially useful if there is no default label for a property. Users can also add their own labels.

## Topics

### Constants
- [let kABWorkLabel: CFString!](kabworklabel.md)
  All Work labels match this label.
- [let kABHomeLabel: CFString!](kabhomelabel.md)
  All Home labels match this label.
- [let kABOtherLabel: CFString!](kabotherlabel.md)
  All labels other than Home or Work labels match this label.
- [let kABMobileMeLabel: String](kabmobilemelabel.md)
  MobileMe instant messenger or email values.

## See Also

- [Address Keys](address-keys.md)
  The keys used to specify the different fields in a `kABAddressProperty`.
- [Default Person Properties](default-person-properties.md)
  The properties that a person record contains by default.
- [Default Group Properties](default-group-properties.md)
  The properties that a group record contains by default.  Developers can add their own properties with the `ABGroup` method [`addPropertiesAndTypes(_:)`](abgroup/addpropertiesandtypes(_:).md)
- [Default Multivalue List Labels](default-multivalue-list-labels.md)
  The default labels contained in the Address Book database for specifying different values in a multivalue list. Users can also add their own labels.
- [Multivalue Property](multivalue-property.md)
  A multivalue property type.
- [Default Record Properties](default-record-properties.md)
  Properties common to all types of records.
- [Property Types](property_types.md)
  The possible [`ABPropertyType`](abpropertytype.md) types for `ABRecord` properties:


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/generic-multivalue-list-labels)*