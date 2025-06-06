# Contact Keys

**Framework**: Contacts

Specify contact-related properties during fetch operations.

## Topics

### Contact Identification
- [let CNContactIdentifierKey: String](cncontactidentifierkey.md)
  The contact’s unique identifier.
- [let CNContactTypeKey: String](cncontacttypekey.md)
  The type of contact.
- [let CNContactPropertyAttribute: String](cncontactpropertyattribute.md)
  The contact’s name component property key.
### Name
- [let CNContactNamePrefixKey: String](cncontactnameprefixkey.md)
  The prefix for the contact’s name.
- [let CNContactGivenNameKey: String](cncontactgivennamekey.md)
  The contact’s given name.
- [let CNContactMiddleNameKey: String](cncontactmiddlenamekey.md)
  The contact’s middle name.
- [let CNContactFamilyNameKey: String](cncontactfamilynamekey.md)
  The contact’s family name.
- [let CNContactPreviousFamilyNameKey: String](cncontactpreviousfamilynamekey.md)
  The contact’s previous family name.
- [let CNContactNameSuffixKey: String](cncontactnamesuffixkey.md)
  The contact’s name suffix.
- [let CNContactNicknameKey: String](cncontactnicknamekey.md)
  The contact’s nickname.
- [let CNContactPhoneticGivenNameKey: String](cncontactphoneticgivennamekey.md)
  The phonetic spelling of the contact’s  given name.
- [let CNContactPhoneticMiddleNameKey: String](cncontactphoneticmiddlenamekey.md)
  The phonetic spelling of the contact’s middle name.
- [let CNContactPhoneticFamilyNameKey: String](cncontactphoneticfamilynamekey.md)
  The phonetic spelling of the contact’s family name.
### Work
- [let CNContactJobTitleKey: String](cncontactjobtitlekey.md)
  The contact’s job title.
- [let CNContactDepartmentNameKey: String](cncontactdepartmentnamekey.md)
  The contact’s department name.
- [let CNContactOrganizationNameKey: String](cncontactorganizationnamekey.md)
  The contact’s organization name.
- [let CNContactPhoneticOrganizationNameKey: String](cncontactphoneticorganizationnamekey.md)
  The phonetic spelling of the contact’s organization name.
### Addresses
- [let CNContactPostalAddressesKey: String](cncontactpostaladdresseskey.md)
  The postal addresses of the contact.
- [let CNContactEmailAddressesKey: String](cncontactemailaddresseskey.md)
  The email addresses of the contact.
- [let CNContactUrlAddressesKey: String](cncontacturladdresseskey.md)
  The URL addresses of the contact.
- [let CNContactInstantMessageAddressesKey: String](cncontactinstantmessageaddresseskey.md)
  The instant message addresses of the contact.
### Phone
- [let CNContactPhoneNumbersKey: String](cncontactphonenumberskey.md)
  A phone numbers of a contact.
### Social Profiles
- [let CNContactSocialProfilesKey: String](cncontactsocialprofileskey.md)
  A social profiles of a contact.
### Birthday
- [let CNContactBirthdayKey: String](cncontactbirthdaykey.md)
  The birthday of a contact.
- [let CNContactNonGregorianBirthdayKey: String](cncontactnongregorianbirthdaykey.md)
  The non-Gregorian birthday of the contact.
- [let CNContactDatesKey: String](cncontactdateskey.md)
  Dates associated with a contact.
### Notes
- [let CNContactNoteKey: String](cncontactnotekey.md)
  A note associated with a contact.
- [com.apple.developer.contacts.notes](../BundleResources/Entitlements/com.apple.developer.contacts.notes.md)
  A Boolean value that indicates whether the app may access the notes in contact entries.
### Images
- [let CNContactImageDataKey: String](cncontactimagedatakey.md)
  Image data for a contact.
- [let CNContactThumbnailImageDataKey: String](cncontactthumbnailimagedatakey.md)
  Thumbnail data for a contact.
- [let CNContactImageDataAvailableKey: String](cncontactimagedataavailablekey.md)
  Image data availability for a contact.
### Relationships
- [let CNContactRelationsKey: String](cncontactrelationskey.md)
  The relationships of the contact.
### Groups and Containers
- [let CNGroupNameKey: String](cngroupnamekey.md)
  The name of the group.
- [let CNGroupIdentifierKey: String](cngroupidentifierkey.md)
  The identifier of the group.
- [let CNContainerNameKey: String](cncontainernamekey.md)
  The name of the container.
- [let CNContainerTypeKey: String](cncontainertypekey.md)
  The type of the container.
### Instant Messaging Keys
- [let CNInstantMessageAddressServiceKey: String](cninstantmessageaddressservicekey.md)
  Instant message address service key.
- [let CNInstantMessageAddressUsernameKey: String](cninstantmessageaddressusernamekey.md)
  Instant message address username key.
### Social Profile Keys
- [let CNSocialProfileServiceKey: String](cnsocialprofileservicekey.md)
  The social profile service.
- [let CNSocialProfileURLStringKey: String](cnsocialprofileurlstringkey.md)
  The social profile URL.
- [let CNSocialProfileUsernameKey: String](cnsocialprofileusernamekey.md)
  The social profile user name.
- [let CNSocialProfileUserIdentifierKey: String](cnsocialprofileuseridentifierkey.md)
  The social profile user identifier.
### Key Descriptors
- [protocol CNKeyDescriptor](cnkeydescriptor.md)
  This protocol is reserved for Contacts framework usage.

## See Also

- [class CNContact](cncontact.md)
  An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.
- [class CNMutableContact](cnmutablecontact.md)
  A mutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.
- [Data Objects](data-objects.md)
  Access contact-related data, such as the user’s postal address and phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/contact-keys)*