# CNMutableContact

**Framework**: Contacts  
**Kind**: class

A mutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNMutableContact
```

#### Overview

`CNMutableContact` objects are not a thread-safe class. To access the contact information in a thread-safe manner, use a [`CNContact`](cncontact.md) object instead.

You may modify only those properties whose values you fetched from the contacts database. When fetching a contact, you specify which properties you want to retrieve from the database. The contact store then populates the properties of a [`CNContact`](cncontact.md) object with those values. After creating a mutable copy of that object, you can modify only those properties for which a value exists. If you attempt to access a property that is not available, the `CNMutableContact` object throws a [`CNContactPropertyNotFetchedExceptionName`](cncontactpropertynotfetchedexceptionname.md) exception.

To remove the value for a property, set string and array properties to empty, and set all other properties to `nil`.

## Topics

### Setting the Identity of the Contact
- [var contactType: CNContactType](cnmutablecontact/contacttype.md)
  An enum identifying the contact type.
### Setting Name Information
- [var namePrefix: String](cnmutablecontact/nameprefix.md)
  The name prefix of the contact.
- [var givenName: String](cnmutablecontact/givenname.md)
  The given name of the contact.
- [var middleName: String](cnmutablecontact/middlename.md)
  The middle name of the contact.
- [var familyName: String](cnmutablecontact/familyname.md)
  The family name of the contact.
- [var previousFamilyName: String](cnmutablecontact/previousfamilyname.md)
  The previous family name of the contact.
- [var nameSuffix: String](cnmutablecontact/namesuffix.md)
  The name suffix of the contact.
- [var nickname: String](cnmutablecontact/nickname.md)
  The nickname of the contact.
- [var phoneticGivenName: String](cnmutablecontact/phoneticgivenname.md)
  The phonetic given name of the contact.
- [var phoneticMiddleName: String](cnmutablecontact/phoneticmiddlename.md)
  The phonetic middle name of the contact.
- [var phoneticFamilyName: String](cnmutablecontact/phoneticfamilyname.md)
  The phonetic family name of the contact.
### Setting Work Information
- [var jobTitle: String](cnmutablecontact/jobtitle.md)
  The contact’s job title.
- [var departmentName: String](cnmutablecontact/departmentname.md)
  The name of the department associated with the contact.
- [var organizationName: String](cnmutablecontact/organizationname.md)
  The name of the organization associated with the contact.
- [var phoneticOrganizationName: String](cnmutablecontact/phoneticorganizationname.md)
  The phonetic name of the organization associated with the contact.
### Setting Addresses
- [var postalAddresses: [CNLabeledValue<CNPostalAddress>]](cnmutablecontact/postaladdresses.md)
  An array of labeled postal addresses for a contact.
- [var emailAddresses: [CNLabeledValue<NSString>]](cnmutablecontact/emailaddresses.md)
  An array of labeled email addresses for the contact.
- [var urlAddresses: [CNLabeledValue<NSString>]](cnmutablecontact/urladdresses.md)
  An array of labeled URL addresses for a contact.
### Setting Phone Information
- [var phoneNumbers: [CNLabeledValue<CNPhoneNumber>]](cnmutablecontact/phonenumbers.md)
  An array of labeled phone numbers for a contact.
### Setting Social Profiles
- [var socialProfiles: [CNLabeledValue<CNSocialProfile>]](cnmutablecontact/socialprofiles.md)
  An array of labeled social profiles for a contact.
### Setting Birthday Information
- [var dates: [CNLabeledValue<NSDateComponents>]](cnmutablecontact/dates.md)
  An array containing labeled Gregorian dates.
- [var nonGregorianBirthday: DateComponents?](cnmutablecontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.
- [var birthday: DateComponents?](cnmutablecontact/birthday.md)
  A date component for the Gregorian birthday of the contact.
### Setting Notes
- [var note: String](cnmutablecontact/note.md)
  A string containing notes for the contact.
### Setting Images
- [var imageData: Data?](cnmutablecontact/imagedata.md)
  The profile picture of a contact.
### Relating Other Information to the Contact
- [var contactRelations: [CNLabeledValue<CNContactRelation>]](cnmutablecontact/contactrelations.md)
  An array of labeled contact relations for the contact.
- [var instantMessageAddresses: [CNLabeledValue<CNInstantMessageAddress>]](cnmutablecontact/instantmessageaddresses.md)
  An array of labeled IM addresses for the contact.
### Instance Properties
- [var id: UUID](cnmutablecontact/id.md)

## Relationships

### Inherits From
- [CNContact](cncontact.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNContact](cncontact.md)
  An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.
- [Data Objects](data-objects.md)
  Access contact-related data, such as the user’s postal address and phone number.
- [Contact Keys](contact-keys.md)
  Specify contact-related properties during fetch operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact)*