# Default Person Properties

**Framework**: Address Book

The properties that a person record contains by default.

#### Overview

You can add your own properties with the `ABPerson` method [`addPropertiesAndTypes(_:)`](abperson/addpropertiesandtypes(_:).md).

## Topics

### Constants
- [let kABFirstNameProperty: String](kabfirstnameproperty.md)
  First name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABLastNameProperty: String](kablastnameproperty.md)
  Last name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABFirstNamePhoneticProperty: String](kabfirstnamephoneticproperty.md)
  Phonetic representation of the first name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABLastNamePhoneticProperty: String](kablastnamephoneticproperty.md)
  Phonetic representation of the last name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABNicknameProperty: String](kabnicknameproperty.md)
  Nickname. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABMaidenNameProperty: String](kabmaidennameproperty.md)
  Maiden name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABBirthdayProperty: String](kabbirthdayproperty.md)
  Birth date. Type: [`kABDateProperty`](kabdateproperty.md).
- [let kABBirthdayComponentsProperty: String](kabbirthdaycomponentsproperty.md)
  Birth date as date components. Type: [`kABDateComponentsProperty`](kabdatecomponentsproperty.md).
- [let kABOrganizationProperty: String](kaborganizationproperty.md)
  Company name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABJobTitleProperty: String](kabjobtitleproperty.md)
  Job title. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABHomePageProperty: String](kabhomepageproperty.md)
  Home web page. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABURLsProperty: String](kaburlsproperty.md)
  Web pages. Type: [`kABMultiStringProperty`](kabmultistringproperty.md).
- [let kABCalendarURIsProperty: String](kabcalendarurisproperty.md)
  Calendar URIs. Type: [`kABMultiStringProperty`](kabmultistringproperty.md).
- [let kABEmailProperty: String](kabemailproperty.md)
  Email addresses. Type: [`kABMultiStringProperty`](kabmultistringproperty.md).
- [let kABAddressProperty: String](kabaddressproperty.md)
  Street addresses. Type: [`kABMultiDictionaryProperty`](kabmultidictionaryproperty.md).
- [let kABOtherDatesProperty: String](kabotherdatesproperty.md)
  Dates associated with a person. Type: [`kABMultiDateProperty`](kabmultidateproperty.md).
- [let kABOtherDateComponentsProperty: String](kabotherdatecomponentsproperty.md)
  Dates associated with a person, as date components. Type: [`kABMultiDateComponentsProperty`](kabmultidatecomponentsproperty.md).
- [let kABRelatedNamesProperty: String](kabrelatednamesproperty.md)
  Names of people related to a person.
- [let kABDepartmentProperty: String](kabdepartmentproperty.md)
  Department name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABPersonFlags: String](kabpersonflags.md)
  Property that specifies the name ordering and configuration of a record in the Address Book application.
- [let kABPhoneProperty: String](kabphoneproperty.md)
  Generic phone number.
- [let kABInstantMessageProperty: String](kabinstantmessageproperty.md)
  Instant messaging ID.
- [let kABNoteProperty: String](kabnoteproperty.md)
  Notes. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABSocialProfileProperty: String](kabsocialprofileproperty.md)
  Social network profile.
- [let kABMiddleNameProperty: String](kabmiddlenameproperty.md)
  Middle name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABMiddleNamePhoneticProperty: String](kabmiddlenamephoneticproperty.md)
  Phonetic representation of the middle name. Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABTitleProperty: String](kabtitleproperty.md)
  Title, such as “Mr.,” “Mrs.,” “General,” “Cardinal,” or “Lord.” Type: [`kABStringProperty`](kabstringproperty.md).
- [let kABSuffixProperty: String](kabsuffixproperty.md)
  Suffix, such as “Sr.,” “Jr.,” “III.,” or “Esq.” Type: [`kABStringProperty`](kabstringproperty.md).

## See Also

- [Address Keys](address-keys.md)
  The keys used to specify the different fields in a `kABAddressProperty`.
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
- [Property Types](property_types.md)
  The possible [`ABPropertyType`](abpropertytype.md) types for `ABRecord` properties:


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/default-person-properties)*