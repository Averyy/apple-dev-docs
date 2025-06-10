# Address Book Constants

**Framework**: Address Book

Get the constants you use to specify Address Book information.

## Topics

### Data Type Constants
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
- [Property Types](property_types.md)
  The possible [`ABPropertyType`](abpropertytype.md) types for `ABRecord` properties:
### Social Media Constants
- [Instant Messaging Keys](instant-messaging-keys.md)
  The keys used to specify the different fields in a [`kABInstantMessageProperty`](kabinstantmessageproperty.md) property.
- [Instant Messaging Services](instant-messaging-services.md)
  The predefined constants are used to identify instant messaging services.
- [Social Profile Services](social-profile-services.md)
  The predefined constants are used to identify social networking services.
### Errors
- [let ABAddressBookErrorDomain: CFString!](abaddressbookerrordomain.md)
  Error domain returning errors reported by an address book object.
- [Error Codes](error-codes.md)
  Errors codes used by the Address Book framework.
### Miscellaneous
- [var ABMultipleValueSelection: ABPeoplePickerSelectionBehavior](abmultiplevalueselection.md)
  The user can select multiple values.
- [var ABNoValueSelection: ABPeoplePickerSelectionBehavior](abnovalueselection.md)
  The user cannot select individual values.
- [var ABSingleValueSelection: ABPeoplePickerSelectionBehavior](absinglevalueselection.md)
  The user can select a single value.
- [let kABAlternateBirthdayComponentsProperty: String](kabalternatebirthdaycomponentsproperty.md)
  The components that represent a birthday in a non-Gregorian calendar.
- [var kABBitsInBitFieldMatch: _ABSearchComparison](kabbitsinbitfieldmatch.md)
  Search for elements that match the bits in ABPersonFlags.
- [var kABContainsSubString: _ABSearchComparison](kabcontainssubstring.md)
  Search for elements that contain the value.
- [var kABContainsSubStringCaseInsensitive: _ABSearchComparison](kabcontainssubstringcaseinsensitive.md)
  Search for elements that contain the value,ignoring case.
- [var kABDefaultNameOrdering: Int32](kabdefaultnameordering.md)
  Default name ordering (whether a person’s first name or last name is displayed first) in the Address Book application.
- [let kABDeletedRecords: String](kabdeletedrecords.md)
  Records that have been deleted.
- [var kABDoesNotContainSubString: _ABSearchComparison](kabdoesnotcontainsubstring.md)
  Search for elements that do not contain the value.
- [var kABDoesNotContainSubStringCaseInsensitive: _ABSearchComparison](kabdoesnotcontainsubstringcaseinsensitive.md)
  Search for elements that do not contain the value, ignoring case.
- [var kABEqual: _ABSearchComparison](kabequal.md)
  Search for elements that are equal to the value.
- [var kABEqualCaseInsensitive: _ABSearchComparison](kabequalcaseinsensitive.md)
  Search for elements that are equal to the value,ignoring case.
- [var kABFirstNameFirst: Int32](kabfirstnamefirst.md)
  First name is displayed first in Address Book.
- [var kABGreaterThan: _ABSearchComparison](kabgreaterthan.md)
  Search for elements that are greater than thevalue.
- [var kABGreaterThanOrEqual: _ABSearchComparison](kabgreaterthanorequal.md)
  Search for elements that are greater than orequal to the value.
- [let kABInsertedRecords: String](kabinsertedrecords.md)
  Records that have been inserted.
- [var kABLastNameFirst: Int32](kablastnamefirst.md)
  Last name is displayed first in Address Book.
- [var kABLessThan: _ABSearchComparison](kablessthan.md)
  Search for elements that are less than thevalue.
- [var kABLessThanOrEqual: _ABSearchComparison](kablessthanorequal.md)
  Search for elements that are less than or equalto the value.
- [var kABMultiValueInvalidIdentifier: Int32](kabmultivalueinvalididentifier.md)
  Invalid multivalue property.
- [var kABNameOrderingMask: Int32](kabnameorderingmask.md)
  Used in conjunction with `kABDefaultNameOrdering`, `kABFirstNameFirst`, and `kABLastNameFirst` to determine name ordering.
- [var kABNotEqual: _ABSearchComparison](kabnotequal.md)
  Search for elements that are not equal to thevalue.
- [var kABNotEqualCaseInsensitive: _ABSearchComparison](kabnotequalcaseinsensitive.md)
  Search for elements that are not equal to the value, ignoring case.
- [var kABNotWithinIntervalAroundToday: _ABSearchComparison](kabnotwithinintervalaroundtoday.md)
  Search for elements that are  within a time interval (in seconds) forward or backward from today.
- [var kABNotWithinIntervalAroundTodayYearless: _ABSearchComparison](kabnotwithinintervalaroundtodayyearless.md)
  Search for elements that are  within a time interval (in seconds) forward or backward from this day in any year.
- [var kABNotWithinIntervalFromToday: _ABSearchComparison](kabnotwithinintervalfromtoday.md)
  Search for elements that are  within a time interval (in seconds) forward from today.
- [var kABNotWithinIntervalFromTodayYearless: _ABSearchComparison](kabnotwithinintervalfromtodayyearless.md)
  Search for elements that are  within a time interval (in seconds) forward from this day in any year.
- [let kABOrganizationPhoneticProperty: String](kaborganizationphoneticproperty.md)
  The phonetic representation of an organization name.
- [var kABPrefixMatch: _ABSearchComparison](kabprefixmatch.md)
  Search for elements that begin with the value.
- [var kABPrefixMatchCaseInsensitive: _ABSearchComparison](kabprefixmatchcaseinsensitive.md)
  Search for elements that begin with the value, ignoring case.
- [var kABPropertyInvalidID: Int32](kabpropertyinvalidid.md)
  Indicates an invalid value for a property ID.
- [var kABRecordInvalidID: Int32](kabrecordinvalidid.md)
  Records with this ID have not been saved to the Address Book database.
- [var kABSearchAnd: _ABSearchConjunction](kabsearchand.md)
  Join the search elements together with theAND operand.
- [var kABSearchOr: _ABSearchConjunction](kabsearchor.md)
  Join the search elements together with theOR operand.
- [var kABShowAsCompany: Int32](kabshowascompany.md)
  Record is displayed as a company.
- [var kABShowAsMask: Int32](kabshowasmask.md)
  Used in conjunction with `kABShowAsPerson` and `kABShowAsCompany` to determine record configuration.
- [var kABShowAsPerson: Int32](kabshowasperson.md)
  Record is displayed as a person.
- [var kABShowAsResource: Int32](kabshowasresource.md)
  Record is displayed as a resource.
- [var kABShowAsRoom: Int32](kabshowasroom.md)
  Record is displayed as a room.
- [let kABSocialProfileServiceTencentWeibo: String](kabsocialprofileservicetencentweibo.md)
  The user’s Tencent Weibo profile identifier.
- [let kABSocialProfileServiceYelp: String](kabsocialprofileserviceyelp.md)
  The user’s Yelp profile identifier.
- [var kABSourceTypeSearchableMask: Int32](kabsourcetypesearchablemask.md)
  Indicates that a source is searchable.
- [var kABSuffixMatch: _ABSearchComparison](kabsuffixmatch.md)
  Search for elements that end with the value.
- [var kABSuffixMatchCaseInsensitive: _ABSearchComparison](kabsuffixmatchcaseinsensitive.md)
  Search for elements that end with the value, ignoring case.
- [let kABUpdatedRecords: String](kabupdatedrecords.md)
  Records that have been updated.
- [var kABWithinIntervalAroundToday: _ABSearchComparison](kabwithinintervalaroundtoday.md)
  Search for elements that are within a time interval (in seconds) forward or backward from today.
- [var kABWithinIntervalAroundTodayYearless: _ABSearchComparison](kabwithinintervalaroundtodayyearless.md)
  Search for elements that are within a time interval (in seconds) forward or backward from this day in any year.
- [var kABWithinIntervalFromToday: _ABSearchComparison](kabwithinintervalfromtoday.md)
  Search for elements that are within a time interval (in seconds) forward from today.
- [var kABWithinIntervalFromTodayYearless: _ABSearchComparison](kabwithinintervalfromtodayyearless.md)
  Search for elements that are within a time interval (in seconds) forward from this day in any year.
### Deprecated
- [let kABPersonAddressCityKey: CFString!](kabpersonaddresscitykey.md)
  City.
- [let kABPersonAddressCountryCodeKey: CFString!](kabpersonaddresscountrycodekey.md)
  Country code. The value is an ISO country code.
- [let kABPersonAddressCountryKey: CFString!](kabpersonaddresscountrykey.md)
  Country or region.
- [let kABPersonAddressProperty: ABPropertyID](kabpersonaddressproperty.md)
  Identifier for the address multivalue property.
- [let kABPersonAddressStateKey: CFString!](kabpersonaddressstatekey.md)
  State.
- [let kABPersonAddressStreetKey: CFString!](kabpersonaddressstreetkey.md)
  Street.
- [let kABPersonAddressZIPKey: CFString!](kabpersonaddresszipkey.md)
  Zip code.
- [let kABPersonAlternateBirthdayCalendarIdentifierKey: CFString!](kabpersonalternatebirthdaycalendaridentifierkey.md)
  The associated value is a string representing the calendar identifier for a [`CFCalendar`](https://developer.apple.com/documentation/CoreFoundation/CFCalendar).
- [let kABPersonAlternateBirthdayDayKey: CFString!](kabpersonalternatebirthdaydaykey.md)
  The associated value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of type [`CFNumberType.nsIntegerType`](https://developer.apple.com/documentation/CoreFoundation/CFNumberType/nsIntegerType) whose value is the day for the birthday.
- [let kABPersonAlternateBirthdayEraKey: CFString!](kabpersonalternatebirthdayerakey.md)
  The associated value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of type [`CFNumberType.nsIntegerType`](https://developer.apple.com/documentation/CoreFoundation/CFNumberType/nsIntegerType) whose value is the era for the birthday.
- [let kABPersonAlternateBirthdayIsLeapMonthKey: CFString!](kabpersonalternatebirthdayisleapmonthkey.md)
  The associated value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of type [`CFNumberType.charType`](https://developer.apple.com/documentation/CoreFoundation/CFNumberType/charType).
- [let kABPersonAlternateBirthdayMonthKey: CFString!](kabpersonalternatebirthdaymonthkey.md)
  The associated value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of type [`CFNumberType.nsIntegerType`](https://developer.apple.com/documentation/CoreFoundation/CFNumberType/nsIntegerType) whose value is the month for the birthday.
- [let kABPersonAlternateBirthdayProperty: ABPropertyID](kabpersonalternatebirthdayproperty.md)
  The associated value is a [`kABDictionaryPropertyType`](kabdictionarypropertytype.md) with keys specified by the other constants listed here.
- [let kABPersonAlternateBirthdayYearKey: CFString!](kabpersonalternatebirthdayyearkey.md)
  The associated value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) of type [`CFNumberType.nsIntegerType`](https://developer.apple.com/documentation/CoreFoundation/CFNumberType/nsIntegerType) whose value is the year for the birthday.
- [let kABPersonAnniversaryLabel: CFString!](kabpersonanniversarylabel.md)
  Birthdate.
- [let kABPersonAssistantLabel: CFString!](kabpersonassistantlabel.md)
  Assistant.
- [let kABPersonBirthdayProperty: ABPropertyID](kabpersonbirthdayproperty.md)
  Birthday. Type: [`kABDateTimePropertyType`](kabdatetimepropertytype.md).
- [let kABPersonBrotherLabel: CFString!](kabpersonbrotherlabel.md)
  Brother.
- [let kABPersonChildLabel: CFString!](kabpersonchildlabel.md)
  Child.
- [let kABPersonCreationDateProperty: ABPropertyID](kabpersoncreationdateproperty.md)
  Creation date. Type: [`kABDateTimePropertyType`](kabdatetimepropertytype.md).
- [let kABPersonDateProperty: ABPropertyID](kabpersondateproperty.md)
  Identifier for the dates multivalue property.
- [let kABPersonDepartmentProperty: ABPropertyID](kabpersondepartmentproperty.md)
  Department. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonEmailProperty: ABPropertyID](kabpersonemailproperty.md)
  Email address. Type: [`kABMultiStringPropertyType`](kabmultistringpropertytype.md).
- [let kABPersonFatherLabel: CFString!](kabpersonfatherlabel.md)
  Father.
- [let kABPersonFirstNamePhoneticProperty: ABPropertyID](kabpersonfirstnamephoneticproperty.md)
  First name phonetic. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonFirstNameProperty: ABPropertyID](kabpersonfirstnameproperty.md)
  First name. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonFriendLabel: CFString!](kabpersonfriendlabel.md)
  Friend.
- [let kABPersonHomePageLabel: CFString!](kabpersonhomepagelabel.md)
  Home page.
- [var kABPersonImageFormatOriginalSize: ABPersonImageFormat](kabpersonimageformatoriginalsize.md)
  The image at its original size and shape.
- [var kABPersonImageFormatThumbnail: ABPersonImageFormat](kabpersonimageformatthumbnail.md)
  The small square thumbnail.
- [let kABPersonInstantMessageProperty: ABPropertyID](kabpersoninstantmessageproperty.md)
  Identifier for the instant message multivalue property.
- [let kABPersonInstantMessageServiceAIM: CFString!](kabpersoninstantmessageserviceaim.md)
  AIM instant message service.
- [let kABPersonInstantMessageServiceFacebook: CFString!](kabpersoninstantmessageservicefacebook.md)
  Facebook instant message service.
- [let kABPersonInstantMessageServiceGaduGadu: CFString!](kabpersoninstantmessageservicegadugadu.md)
  Gadu-Gadu instant message service.
- [let kABPersonInstantMessageServiceGoogleTalk: CFString!](kabpersoninstantmessageservicegoogletalk.md)
  Google Talk instant message service.
- [let kABPersonInstantMessageServiceICQ: CFString!](kabpersoninstantmessageserviceicq.md)
  ICQ instant message service.
- [let kABPersonInstantMessageServiceJabber: CFString!](kabpersoninstantmessageservicejabber.md)
  Jabber instant message service.
- [let kABPersonInstantMessageServiceKey: CFString!](kabpersoninstantmessageservicekey.md)
  Instant message service.
- [let kABPersonInstantMessageServiceMSN: CFString!](kabpersoninstantmessageservicemsn.md)
  MSN instant message service.
- [let kABPersonInstantMessageServiceQQ: CFString!](kabpersoninstantmessageserviceqq.md)
  QQ instant message service.
- [let kABPersonInstantMessageServiceSkype: CFString!](kabpersoninstantmessageserviceskype.md)
  Skype instant message service.
- [let kABPersonInstantMessageServiceYahoo: CFString!](kabpersoninstantmessageserviceyahoo.md)
  Yahoo instant message service.
- [let kABPersonInstantMessageUsernameKey: CFString!](kabpersoninstantmessageusernamekey.md)
  Instant message service username.
- [let kABPersonJobTitleProperty: ABPropertyID](kabpersonjobtitleproperty.md)
  Job title. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonKindOrganization: CFNumber!](kabpersonkindorganization.md)
  Identifies an organization.
- [let kABPersonKindPerson: CFNumber!](kabpersonkindperson.md)
  Identifies a person.
- [let kABPersonKindProperty: ABPropertyID](kabpersonkindproperty.md)
  Identifier for the type property.
- [let kABPersonLastNamePhoneticProperty: ABPropertyID](kabpersonlastnamephoneticproperty.md)
  Last name phonetic. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonLastNameProperty: ABPropertyID](kabpersonlastnameproperty.md)
  Last name. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonManagerLabel: CFString!](kabpersonmanagerlabel.md)
  Manager.
- [let kABPersonMiddleNamePhoneticProperty: ABPropertyID](kabpersonmiddlenamephoneticproperty.md)
  Middle name phonetic. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonMiddleNameProperty: ABPropertyID](kabpersonmiddlenameproperty.md)
  Middle name. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonModificationDateProperty: ABPropertyID](kabpersonmodificationdateproperty.md)
  Modification date. Type: [`kABDateTimePropertyType`](kabdatetimepropertytype.md).
- [let kABPersonMotherLabel: CFString!](kabpersonmotherlabel.md)
  Mother.
- [let kABPersonNicknameProperty: ABPropertyID](kabpersonnicknameproperty.md)
  Nickname. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonNoteProperty: ABPropertyID](kabpersonnoteproperty.md)
  Note. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonOrganizationProperty: ABPropertyID](kabpersonorganizationproperty.md)
  Organization name. Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonParentLabel: CFString!](kabpersonparentlabel.md)
  Parent.
- [let kABPersonPartnerLabel: CFString!](kabpersonpartnerlabel.md)
  Partner.
- [let kABPersonPhoneHomeFAXLabel: CFString!](kabpersonphonehomefaxlabel.md)
  Home fax number.
- [let kABPersonPhoneIPhoneLabel: CFString!](kabpersonphoneiphonelabel.md)
  iPhone number.
- [let kABPersonPhoneMainLabel: CFString!](kabpersonphonemainlabel.md)
  Main phone number.
- [let kABPersonPhoneMobileLabel: CFString!](kabpersonphonemobilelabel.md)
  Mobile phone number.
- [let kABPersonPhoneOtherFAXLabel: CFString!](kabpersonphoneotherfaxlabel.md)
  Other fax number.
- [let kABPersonPhonePagerLabel: CFString!](kabpersonphonepagerlabel.md)
  Pager phone number.
- [let kABPersonPhoneProperty: ABPropertyID](kabpersonphoneproperty.md)
  Identifier for the phone number multivalue property.
- [let kABPersonPhoneWorkFAXLabel: CFString!](kabpersonphoneworkfaxlabel.md)
  Work fax number.
- [let kABPersonPrefixProperty: ABPropertyID](kabpersonprefixproperty.md)
  Prefix (“Sir,” “Duke,” “General”). Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonRelatedNamesProperty: ABPropertyID](kabpersonrelatednamesproperty.md)
  Identifier for the related name multivalue property.
- [let kABPersonSisterLabel: CFString!](kabpersonsisterlabel.md)
  Sister.
- [let kABPersonSocialProfileProperty: ABPropertyID](kabpersonsocialprofileproperty.md)
  Identifier for the social profile property.
- [let kABPersonSocialProfileServiceFacebook: CFString!](kabpersonsocialprofileservicefacebook.md)
  Facebook social profile service.
- [let kABPersonSocialProfileServiceFlickr: CFString!](kabpersonsocialprofileserviceflickr.md)
  Flickr social profile service.
- [let kABPersonSocialProfileServiceGameCenter: CFString!](kabpersonsocialprofileservicegamecenter.md)
  Game Center social profile service.
- [let kABPersonSocialProfileServiceKey: CFString!](kabpersonsocialprofileservicekey.md)
  Social profile service.
- [let kABPersonSocialProfileServiceLinkedIn: CFString!](kabpersonsocialprofileservicelinkedin.md)
  LinkedIn social profile service.
- [let kABPersonSocialProfileServiceMyspace: CFString!](kabpersonsocialprofileservicemyspace.md)
  Myspace social profile service.
- [let kABPersonSocialProfileServiceSinaWeibo: CFString!](kabpersonsocialprofileservicesinaweibo.md)
  Sina Weibo social profile service.
- [let kABPersonSocialProfileServiceTwitter: CFString!](kabpersonsocialprofileservicetwitter.md)
  Twitter social profile service.
- [let kABPersonSocialProfileURLKey: CFString!](kabpersonsocialprofileurlkey.md)
  Social profile URL.
- [let kABPersonSocialProfileUserIdentifierKey: CFString!](kabpersonsocialprofileuseridentifierkey.md)
  Social profile user identifier.
- [let kABPersonSocialProfileUsernameKey: CFString!](kabpersonsocialprofileusernamekey.md)
  Social profile username.
- [let kABPersonSpouseLabel: CFString!](kabpersonspouselabel.md)
  Spouse.
- [let kABPersonSuffixProperty: ABPropertyID](kabpersonsuffixproperty.md)
  Suffix (“Jr.,” “Sr.,” “III”). Type: [`kABStringPropertyType`](kabstringpropertytype.md).
- [let kABPersonURLProperty: ABPropertyID](kabpersonurlproperty.md)
  Identifier for the URL multivalue property.
- [let kABSourceNameProperty: ABPropertyID](kabsourcenameproperty.md)
  The name of the source. Type: kABStringPropertyType.
- [let kABSourceTypeProperty: ABPropertyID](kabsourcetypeproperty.md)
  The type of the source.

## See Also

- [C Types](c-types.md)
  Identify the C types that correspond to Address Book objects.
- [AddressBook Functions](addressbook-functions.md)
  Find the C functions and function-like macros you use to manipulate Address Book data.
- [AddressBook Enumerations](addressbook-enumerations.md)
  Get the enumerations you use to specify Address Book information.
- [AddressBook Data Types](addressbook-data-types.md)
  Get the data types you use to specify Address Book information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/address-book-constants)*