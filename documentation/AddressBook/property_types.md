# Property Types

**Framework**: Address Book

The possible [`ABPropertyType`](abpropertytype.md) types for `ABRecord` properties:

## Topics

### Constants
- [var kABErrorInProperty: _ABPropertyType](kaberrorinproperty.md)
  An invalid property was used.
- [var kABStringProperty: _ABPropertyType](kabstringproperty.md)
  This property is an `NSString` object.
- [var kABIntegerProperty: _ABPropertyType](kabintegerproperty.md)
  This property is an `NSNumber` object representing an integer.
- [var kABRealProperty: _ABPropertyType](kabrealproperty.md)
  This property is an `NSNumber` object representing a real number.
- [var kABDateProperty: _ABPropertyType](kabdateproperty.md)
  This property is an `NSDate` object.
- [var kABArrayProperty: _ABPropertyType](kabarrayproperty.md)
  This property is an `NSArray` object.
- [var kABDictionaryProperty: _ABPropertyType](kabdictionaryproperty.md)
  This property is an `NSDictionary` object.
- [var kABDataProperty: _ABPropertyType](kabdataproperty.md)
  This property is an `NSData` object.
- [var kABDateComponentsProperty: _ABPropertyType](kabdatecomponentsproperty.md)
  This property is an `NSDateComponents` object.
- [var kABMultiStringProperty: _ABPropertyType](kabmultistringproperty.md)
  This property is an `ABMultiValue` object containing `NSString` objects.
- [var kABMultiIntegerProperty: _ABPropertyType](kabmultiintegerproperty.md)
  This property is an `ABMultiValue` object containing `NSNumber` objects representing integers.
- [var kABMultiRealProperty: _ABPropertyType](kabmultirealproperty.md)
  This property is an `ABMultiValue` object containing `NSNumber` objects representing real numbers.
- [var kABMultiDateProperty: _ABPropertyType](kabmultidateproperty.md)
  This property is an `ABMultiValue` object containing `NSDate` objects.
- [var kABMultiArrayProperty: _ABPropertyType](kabmultiarrayproperty.md)
  This property is an `ABMultiValue` object containing `NSArray` objects.
- [var kABMultiDictionaryProperty: _ABPropertyType](kabmultidictionaryproperty.md)
  This property is an `ABMultiValue` object containing `NSDictionary` objects.
- [var kABMultiDataProperty: _ABPropertyType](kabmultidataproperty.md)
  This property is an `ABMultiValue` object containing `NSData` objects.
- [var kABMultiDateComponentsProperty: _ABPropertyType](kabmultidatecomponentsproperty.md)
  This property is an `ABMultiValue` object containing `NSDateComponents` objects.

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
- [Default Record Properties](default-record-properties.md)
  Properties common to all types of records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/property_types)*