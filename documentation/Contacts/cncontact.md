# CNContact

**Framework**: Contacts  
**Kind**: class

An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContact
```

#### Overview

A `CNContact` object stores an immutable copy of a contact’s information, so you cannot change the information in this object directly. Contact objects are thread-safe, so you may access them from any thread of your app.

To modify a contact’s information, call the [`mutableCopy()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/mutableCopy()) method to obtain a [`CNMutableContact`](cnmutablecontact.md) object with the same information. After modifying the mutable contact, save your changes back to the contacts database using the [`CNContactStore`](cncontactstore.md) object.

Every contact in the contacts database has a unique ID, which you access using the [`identifier`](cncontact/identifier.md) property. The mutable and immutable versions of the same contact have the same identifier.

## Topics

### Identifying the Contact
- [var identifier: String](cncontact/identifier.md)
  A value that uniquely identifies a contact on the device.
- [var contactType: CNContactType](cncontact/contacttype.md)
  An enum identifying the contact type.
- [enum CNContactType](cncontacttype.md)
  The types a contact can be.
### Getting Name Information
- [var namePrefix: String](cncontact/nameprefix.md)
  The name prefix of the contact.
- [var givenName: String](cncontact/givenname.md)
  The given name of the contact.
- [var middleName: String](cncontact/middlename.md)
  The middle name of the contact.
- [var familyName: String](cncontact/familyname.md)
  The family name of the contact.
- [var previousFamilyName: String](cncontact/previousfamilyname.md)
  A string for the previous family name of the contact.
- [var nameSuffix: String](cncontact/namesuffix.md)
  The name suffix of the contact.
- [var nickname: String](cncontact/nickname.md)
  The nickname of the contact.
- [var phoneticGivenName: String](cncontact/phoneticgivenname.md)
  The phonetic given name of the contact.
- [var phoneticMiddleName: String](cncontact/phoneticmiddlename.md)
  The phonetic middle name of the contact.
- [var phoneticFamilyName: String](cncontact/phoneticfamilyname.md)
  A string for the phonetic family name of the contact.
### Getting Work Information
- [var jobTitle: String](cncontact/jobtitle.md)
  The contact’s job title.
- [var departmentName: String](cncontact/departmentname.md)
  The name of the department associated with the contact.
- [var organizationName: String](cncontact/organizationname.md)
  The name of the organization associated with the contact.
- [var phoneticOrganizationName: String](cncontact/phoneticorganizationname.md)
  The phonetic name of the organization associated with the contact.
### Getting Addresses
- [var postalAddresses: [CNLabeledValue<CNPostalAddress>]](cncontact/postaladdresses.md)
  An array of labeled postal addresses for a contact.
- [var emailAddresses: [CNLabeledValue<NSString>]](cncontact/emailaddresses.md)
  An array of labeled email addresses for the contact.
- [var urlAddresses: [CNLabeledValue<NSString>]](cncontact/urladdresses.md)
  An array of labeled URL addresses for a contact.
### Getting Phone Information
- [var phoneNumbers: [CNLabeledValue<CNPhoneNumber>]](cncontact/phonenumbers.md)
  An array of labeled phone numbers for a contact.
### Getting Social Profiles
- [var socialProfiles: [CNLabeledValue<CNSocialProfile>]](cncontact/socialprofiles.md)
  An array of labeled social profiles for a contact.
### Getting Birthday Information
- [var birthday: DateComponents?](cncontact/birthday.md)
  A date component for the Gregorian birthday of the contact.
- [var nonGregorianBirthday: DateComponents?](cncontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.
- [var dates: [CNLabeledValue<NSDateComponents>]](cncontact/dates.md)
  An array containing labeled Gregorian dates.
### Getting Notes
- [var note: String](cncontact/note.md)
  A string containing notes for the contact.
### Getting Contact Images
- [var imageData: Data?](cncontact/imagedata.md)
  The profile picture of a contact.
- [var thumbnailImageData: Data?](cncontact/thumbnailimagedata.md)
  The thumbnail version of the contact’s profile picture.
- [var imageDataAvailable: Bool](cncontact/imagedataavailable.md)
  A Boolean indicating whether a contact has a profile picture.
### Getting Related Information
- [var contactRelations: [CNLabeledValue<CNContactRelation>]](cncontact/contactrelations.md)
  An array of labeled relations for the contact.
- [var instantMessageAddresses: [CNLabeledValue<CNInstantMessageAddress>]](cncontact/instantmessageaddresses.md)
  An array of labeled IM addresses for the contact.
### Localizing Contact Data
- [class func localizedString(forKey: String) -> String](cncontact/localizedstring(forkey:).md)
  Returns a string containing the localized contact property name.
### Comparing Contacts
- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](cncontact/descriptorforallcomparatorkeys.md)
  Fetches all the keys required for the contact sort comparator.
- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](cncontact/comparator(fornamesortorder:).md)
  Returns a comparator to sort contacts with the specified order.
- [func isUnifiedWithContact(withIdentifier: String) -> Bool](cncontact/isunifiedwithcontact(withidentifier:).md)
  Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.
### Checking the Availability of Data
- [func isKeyAvailable(String) -> Bool](cncontact/iskeyavailable(_:).md)
  Determines whether the contact property value for the specified key is fetched.
- [func areKeysAvailable([any CNKeyDescriptor]) -> Bool](cncontact/arekeysavailable(_:).md)
  Determines whether all contact property values for the specified keys are fetched.
### Getting Search Predicates
- [class func predicateForContacts(matchingName: String) -> NSPredicate](cncontact/predicateforcontacts(matchingname:).md)
  Returns a predicate to find the contacts matching the specified name.
- [class func predicateForContacts(withIdentifiers: [String]) -> NSPredicate](cncontact/predicateforcontacts(withidentifiers:).md)
  Returns a predicate to find the contacts matching the specified identifiers.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsingroup(withidentifier:).md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContactsInContainer(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsincontainer(withidentifier:).md)
  Returns a predicate to find the contacts in the specified container.
- [class func predicateForContacts(matching: CNPhoneNumber) -> NSPredicate](cncontact/predicateforcontacts(matching:).md)
  Returns a predicate to find the contacts whose phone number matches the specified value.
- [class func predicateForContacts(matchingEmailAddress: String) -> NSPredicate](cncontact/predicateforcontacts(matchingemailaddress:).md)
  Returns a predicate to find the contacts whose email address matches the specified value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CNMutableContact](cnmutablecontact.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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

- [class CNMutableContact](cnmutablecontact.md)
  A mutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.
- [Data Objects](data-objects.md)
  Access contact-related data, such as the user’s postal address and phone number.
- [Contact Keys](contact-keys.md)
  Specify contact-related properties during fetch operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact)*