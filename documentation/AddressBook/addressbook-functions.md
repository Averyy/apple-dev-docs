# AddressBook Functions

**Framework**: Address Book

Find the C functions and function-like macros you use to manipulate Address Book data.

## Topics

### Address Book
- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](abgetsharedaddressbook().md)
  Returns the unique shared ABAddressBook object.
- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](abcopydefaultcountrycode(_:).md)
  Returns the default country code for records with unspecified country codes.
- [func ABHasUnsavedChanges(ABAddressBookRef!) -> Bool](abhasunsavedchanges(_:).md)
  Returns whether if there are unsaved changes in the address book.
- [func ABSave(ABAddressBookRef!) -> Bool](absave(_:).md)
  Saves all the changes made since the last save.
### People
- [func ABCopyArrayOfAllPeople(ABAddressBookRef!) -> Unmanaged<CFArray>!](abcopyarrayofallpeople(_:).md)
  Returns an array of all the people in the Address Book database.
- [func ABGetMe(ABAddressBookRef!) -> Unmanaged<ABPersonRef>!](abgetme(_:).md)
  Returns the ABPerson object for the logged-in user.
- [func ABPersonCopyImageData(ABRecord!) -> Unmanaged<CFData>!](abpersoncopyimagedata(_:).md)
  Returns data that contains a picture of a person.
- [func ABPersonCopyParentGroups(ABPersonRef!) -> Unmanaged<CFArray>!](abpersoncopyparentgroups(_:).md)
  Returns an array of groups that a person belongs to.
- [func ABPersonCopyVCardRepresentation(ABPersonRef!) -> Unmanaged<CFData>!](abpersoncopyvcardrepresentation(_:).md)
  Returns the vCard representation of the person as a data object in vCard format.
- [func ABPersonCreate() -> Unmanaged<ABRecord>!](abpersoncreate().md)
  Returns a newly created person object.
- [func ABPersonCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](abpersoncreatesearchelement(_:_:_:_:_:).md)
  Returns a search element object that specifies a query for records of this type.
- [func ABPersonCreateWithVCardRepresentation(CFData!) -> Unmanaged<ABPersonRef>!](abpersoncreatewithvcardrepresentation(_:).md)
  Returns a new ABPerson object initialized with the given data in vCard format.
- [func ABPersonSetImageData(ABRecord!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abpersonsetimagedata(_:_:).md)
  Sets the image for this person to the given data.
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](absetme(_:_:).md)
  Sets the record that represents the logged-in user.
### Groups
- [func ABCopyArrayOfAllGroups(ABAddressBookRef!) -> Unmanaged<CFArray>!](abcopyarrayofallgroups(_:).md)
  Returns an array of all the groups in the Address Book database.
- [func ABGroupAddGroup(ABGroupRef!, ABGroupRef!) -> Bool](abgroupaddgroup(_:_:).md)
  Adds a subgroup to another group.
- [func ABGroupAddMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupaddmember(_:_:).md)
  Adds a person to a group.
- [func ABGroupCopyArrayOfAllMembers(ABRecord!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallmembers(_:).md)
  Returns an array of persons in a group.
- [func ABGroupCopyArrayOfAllSubgroups(ABGroupRef!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallsubgroups(_:).md)
  Returns an array containing a group’s subgroups.
- [func ABGroupCopyDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!) -> Unmanaged<CFString>!](abgroupcopydistributionidentifier(_:_:_:).md)
  Returns the distribution identifier for the given propertyand person.
- [func ABGroupCopyParentGroups(ABGroupRef!) -> Unmanaged<CFArray>!](abgroupcopyparentgroups(_:).md)
  Returns an array containing a group’s parents—thegroups that a group belongs to.
- [func ABGroupCreate() -> Unmanaged<ABRecord>!](abgroupcreate().md)
  Returns a new ABGroup object.
- [func ABGroupCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](abgroupcreatesearchelement(_:_:_:_:_:).md)
  Creates an ABSearchElement object that specifies a queryfor ABGroup records.
- [func ABGroupRemoveGroup(ABGroupRef!, ABGroupRef!) -> Bool](abgroupremovegroup(_:_:).md)
  Removes a subgroup from a group.
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupremovemember(_:_:).md)
  Removes a person from a group.
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](abgroupsetdistributionidentifier(_:_:_:_:).md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).
### Multi Values
- [func ABMultiValueAdd(ABMutableMultiValueRef!, CFTypeRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](abmultivalueadd(_:_:_:_:).md)
  Adds a value and its label to a multi-value list.
- [func ABMultiValueCopyIdentifierAtIndex(ABMultiValueRef!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopyidentifieratindex(_:_:).md)
  Returns the identifier at the given index.
- [func ABMultiValueCopyLabelAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopylabelatindex(_:_:).md)
  Returns the label for the given index.
- [func ABMultiValueCopyPrimaryIdentifier(ABMultiValueRef!) -> Unmanaged<CFString>!](abmultivaluecopyprimaryidentifier(_:).md)
  Returns the identifier for the primary value.
- [func ABMultiValueCopyValueAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFTypeRef>!](abmultivaluecopyvalueatindex(_:_:).md)
  Returns the value for the given index.
- [func ABMultiValueCount(ABMultiValueRef!) -> CFIndex](abmultivaluecount(_:).md)
  Returns the number of entries in a multi-value list.
- [func ABMultiValueCreate() -> Unmanaged<ABMultiValueRef>!](abmultivaluecreate().md)
  Returns a new ABMultiValue object.
- [func ABMultiValueCreateCopy(ABMultiValueRef!) -> Unmanaged<ABMultiValueRef>!](abmultivaluecreatecopy(_:).md)
  Returns a copy of a multi-value object.
- [func ABMultiValueCreateMutable(ABPropertyType) -> Unmanaged<ABMutableMultiValue>!](abmultivaluecreatemutable().md)
  Returns a newly created mutable multi-value list object.
- [func ABMultiValueCreateMutableCopy(ABMultiValue!) -> Unmanaged<ABMutableMultiValue>!](abmultivaluecreatemutablecopy(_:).md)
  Returns a mutable copy of a multi-value object.
- [func ABMultiValueIndexForIdentifier(ABMultiValueRef!, CFString!) -> CFIndex](abmultivalueindexforidentifier(_:_:).md)
  Returns the index for the given identifier.
- [func ABMultiValueInsert(ABMutableMultiValueRef!, CFTypeRef!, CFString!, CFIndex, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](abmultivalueinsert(_:_:_:_:_:).md)
  Inserts a value and its label at the given index in amulti-value list.
- [func ABMultiValuePropertyType(ABMultiValueRef!) -> ABPropertyType](abmultivaluepropertytype(_:).md)
  Returns the type for the values in a multi-value list.
- [func ABMultiValueRemove(ABMutableMultiValueRef!, CFIndex) -> Bool](abmultivalueremove(_:_:).md)
  Removes the value and label at the given index.
- [func ABMultiValueReplaceLabel(ABMutableMultiValueRef!, CFString!, CFIndex) -> Bool](abmultivaluereplacelabel(_:_:_:).md)
  Replaces the label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](abmultivaluereplacevalue(_:_:_:).md)
  Replaces the value at the given index.
- [func ABMultiValueSetPrimaryIdentifier(ABMutableMultiValueRef!, CFString!) -> Bool](abmultivaluesetprimaryidentifier(_:_:).md)
  Sets the primary value to be the value for the given identifier.
### Images
- [func ABBeginLoadingImageDataForClient(ABPersonRef!, ABImageClientCallback!, UnsafeMutableRawPointer!) -> CFIndex](abbeginloadingimagedataforclient(_:_:_:).md)
  Starts an asynchronous fetch for image data in all locations, and returns a non-zero tag for tracking.
- [func ABCancelLoadingImageDataForTag(CFIndex)](abcancelloadingimagedatafortag(_:).md)
  Cancels an asynchronous fetch of an image for the given tag.
### Search Elements
- [func ABCopyArrayOfMatchingRecords(ABAddressBookRef!, ABSearchElementRef!) -> Unmanaged<CFArray>!](abcopyarrayofmatchingrecords(_:_:).md)
  Returns an array of records that match the given search element, or an empty array if no records match the search element.
- [func ABSearchElementCreateWithConjunction(ABSearchConjunction, CFArray!) -> Unmanaged<ABSearchElementRef>!](absearchelementcreatewithconjunction(_:_:).md)
  Returns a compound search element created by combiningthe search elements in an array with the given conjunction.
- [func ABSearchElementMatchesRecord(ABSearchElementRef!, ABRecordRef!) -> Bool](absearchelementmatchesrecord(_:_:).md)
  Tests whether or not a record matches a search element.
### Properties
- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](abaddpropertiesandtypes(_:_:_:).md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](abcopyarrayofpropertiesforrecordtype(_:_:).md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](abcopylocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](ablocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](abremoveproperties(_:_:_:).md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](abtypeofproperty(_:_:_:).md)
  Returns the type of a given property for a given record.
### Records
- [func ABAddRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abaddrecord(_:_:).md)
  Adds a record of the specified type to the Address Book database.
- [func ABCopyRecordForUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<ABRecordRef>!](abcopyrecordforuniqueid(_:_:).md)
  Returns the record that matches the given unique ID.
- [func ABCopyRecordTypeFromUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<CFString>!](abcopyrecordtypefromuniqueid(_:_:).md)
  Returns the type name of the record that matches a given unique ID.
- [func ABCreateFormattedAddressFromDictionary(ABAddressBookRef!, CFDictionary!) -> Unmanaged<CFString>!](abcreateformattedaddressfromdictionary(_:_:).md)
  Returns a string containing the formatted address.
- [func ABRecordCopyRecordType(ABRecordRef!) -> Unmanaged<CFString>!](abrecordcopyrecordtype(_:).md)
  Returns the type of the given record.
- [func ABRecordCopyUniqueId(ABRecordRef!) -> Unmanaged<CFString>!](abrecordcopyuniqueid(_:).md)
  Returns the unique ID of the receiver.
- [func ABRecordCopyValue(ABRecord!, ABPropertyID) -> Unmanaged<CFTypeRef>!](abrecordcopyvalue(_:_:).md)
  Returns the value of the given property.
- [func ABRecordCreateCopy(ABRecordRef!) -> Unmanaged<ABRecordRef>!](abrecordcreatecopy(_:).md)
  Returns a copy of the given record.
- [func ABRecordIsReadOnly(ABRecordRef!) -> Bool](abrecordisreadonly(_:).md)
  Returns whether or not the record is read-only.
- [func ABRecordRemoveValue(ABRecord!, ABPropertyID, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordremovevalue(_:_:).md)
  Removes the value of the given property.
- [func ABRecordSetValue(ABRecord!, ABPropertyID, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordsetvalue(_:_:_:).md)
  Sets the value of a given property for a record.
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abremoverecord(_:_:).md)
  Removes the specified record from the Address Book database.
### Deprecated
- [func ABAddressBookAddRecord(ABAddressBook!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abaddressbookaddrecord(_:_:_:).md)
  Adds a record to an address book.
- [func ABAddressBookCopyArrayOfAllGroups(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallgroups(_:).md)
  Returns an array with all the groups in an address book.
- [func ABAddressBookCopyArrayOfAllGroupsInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallgroupsinsource(_:_:).md)
  Returns an array of all groups from a particular source.
- [func ABAddressBookCopyArrayOfAllPeople(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeople(_:).md)
  Returns all the person records in an address book.
- [func ABAddressBookCopyArrayOfAllPeopleInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeopleinsource(_:_:).md)
  Returns an array of all person records from a particular source.
- [func ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(ABAddressBook!, ABRecord!, ABPersonSortOrdering) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeopleinsourcewithsortordering(_:_:_:).md)
  Returns an array of all person records in the address book, sorted with the specified order.
- [func ABAddressBookCopyArrayOfAllSources(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallsources(_:).md)
  Returns an array of all sources in the address book.
- [func ABAddressBookCopyDefaultSource(ABAddressBook!) -> Unmanaged<ABRecord>!](abaddressbookcopydefaultsource(_:).md)
  Returns the default source.
- [func ABAddressBookCopyLocalizedLabel(CFString!) -> Unmanaged<CFString>!](abaddressbookcopylocalizedlabel(_:).md)
  Returns a localized version of a record-property label.
- [func ABAddressBookCopyPeopleWithName(ABAddressBook!, CFString!) -> Unmanaged<CFArray>!](abaddressbookcopypeoplewithname(_:_:).md)
  Performs a prefix search on the composite names of people in an address book and returns an array of persons that match the search criteria.
- [func ABAddressBookCreate() -> Unmanaged<ABAddressBook>!](abaddressbookcreate().md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookCreateWithOptions(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>!](abaddressbookcreatewithoptions(_:_:).md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus](abaddressbookgetauthorizationstatus().md)
  Returns the authorization status of your app for accessing address book data.
- [func ABAddressBookGetGroupCount(ABAddressBook!) -> CFIndex](abaddressbookgetgroupcount(_:).md)
  Returns the number of groups in an address book.
- [func ABAddressBookGetGroupWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](abaddressbookgetgroupwithrecordid(_:_:).md)
  Returns the group with a given record ID.
- [func ABAddressBookGetPersonCount(ABAddressBook!) -> CFIndex](abaddressbookgetpersoncount(_:).md)
  Returns the number of person records in an address book.
- [func ABAddressBookGetPersonWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](abaddressbookgetpersonwithrecordid(_:_:).md)
  Returns the person record with a given record ID.
- [func ABAddressBookGetSourceWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](abaddressbookgetsourcewithrecordid(_:_:).md)
  Returns the source record with the given record ID.
- [func ABAddressBookHasUnsavedChanges(ABAddressBook!) -> Bool](abaddressbookhasunsavedchanges(_:).md)
  Indicates whether an address book has changes that have not been saved to the Address Book database.
- [func ABAddressBookRegisterExternalChangeCallback(ABAddressBook!, ABExternalChangeCallback!, UnsafeMutableRawPointer!)](abaddressbookregisterexternalchangecallback(_:_:_:).md)
  Registers a callback to receive notifications when the Address Book database is modified.
- [func ABAddressBookRemoveRecord(ABAddressBook!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abaddressbookremoverecord(_:_:_:).md)
  Removes a record from an address book.
- [func ABAddressBookRequestAccessWithCompletion(ABAddressBook!, ABAddressBookRequestAccessCompletionHandler!)](abaddressbookrequestaccesswithcompletion(_:_:).md)
  Requests access to address book data from the user.
- [func ABAddressBookRevert(ABAddressBook!)](abaddressbookrevert(_:).md)
  Discards unsaved changes in an address book.
- [func ABAddressBookSave(ABAddressBook!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abaddressbooksave(_:_:).md)
  Saves any unsaved changes to the Address Book database.
- [func ABAddressBookUnregisterExternalChangeCallback(ABAddressBook!, ABExternalChangeCallback!, UnsafeMutableRawPointer!)](abaddressbookunregisterexternalchangecallback(_:_:_:).md)
  Unregisters a callback.
- [func ABGroupCopyArrayOfAllMembersWithSortOrdering(ABRecord!, ABPersonSortOrdering) -> Unmanaged<CFArray>!](abgroupcopyarrayofallmemberswithsortordering(_:_:).md)
  Returns the records in a group, using a sort ordering.
- [func ABGroupCopySource(ABRecord!) -> Unmanaged<ABRecord>!](abgroupcopysource(_:).md)
  Returns the source that the group is from.
- [func ABGroupCreateInSource(ABRecord!) -> Unmanaged<ABRecord>!](abgroupcreateinsource(_:).md)
  Creates a group in a particular source.
- [func ABMultiValueAddValueAndLabel(ABMutableMultiValue!, CFTypeRef!, CFString!, UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool](abmultivalueaddvalueandlabel(_:_:_:_:).md)
  Adds a value and its corresponding label to a multivalue property.
- [func ABMultiValueCopyArrayOfAllValues(ABMultiValue!) -> Unmanaged<CFArray>!](abmultivaluecopyarrayofallvalues(_:).md)
  Returns an array with the values in a multivalue property.
- [func ABMultiValueGetCount(ABMultiValue!) -> CFIndex](abmultivaluegetcount(_:).md)
  Returns the number of values in a multivalue property.
- [func ABMultiValueGetFirstIndexOfValue(ABMultiValue!, CFTypeRef!) -> CFIndex](abmultivaluegetfirstindexofvalue(_:_:).md)
  Returns the first location of a value in a multivalue property.
- [func ABMultiValueGetIdentifierAtIndex(ABMultiValue!, CFIndex) -> ABMultiValueIdentifier](abmultivaluegetidentifieratindex(_:_:).md)
  Returns the identifier of a value in a multivalue property.
- [func ABMultiValueGetIndexForIdentifier(ABMultiValue!, ABMultiValueIdentifier) -> CFIndex](abmultivaluegetindexforidentifier(_:_:).md)
  Returns the location (within a multivalue property) of a value with a given identifier.
- [func ABMultiValueGetPropertyType(ABMultiValue!) -> ABPropertyType](abmultivaluegetpropertytype(_:).md)
  Returns the type of the values contained in a multivalue property.
- [func ABMultiValueInsertValueAndLabelAtIndex(ABMutableMultiValue!, CFTypeRef!, CFString!, CFIndex, UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool](abmultivalueinsertvalueandlabelatindex(_:_:_:_:_:).md)
  Inserts a value and a label into a multivalue property.
- [func ABMultiValueRemoveValueAndLabelAtIndex(ABMutableMultiValue!, CFIndex) -> Bool](abmultivalueremovevalueandlabelatindex(_:_:).md)
  Removes a value from a multivalue property.
- [func ABMultiValueReplaceLabelAtIndex(ABMutableMultiValue!, CFString!, CFIndex) -> Bool](abmultivaluereplacelabelatindex(_:_:_:).md)
  Replaces a label in a multivalue property with another label.
- [func ABMultiValueReplaceValueAtIndex(ABMutableMultiValue!, CFTypeRef!, CFIndex) -> Bool](abmultivaluereplacevalueatindex(_:_:_:).md)
  Replaces a value in a multivalue property with another value.
- [func ABPersonComparePeopleByName(ABRecord!, ABRecord!, ABPersonSortOrdering) -> CFComparisonResult](abpersoncomparepeoplebyname(_:_:_:).md)
  Indicates how two person records get sorted.
- [func ABPersonCopyArrayOfAllLinkedPeople(ABRecord!) -> Unmanaged<CFArray>!](abpersoncopyarrayofalllinkedpeople(_:).md)
  Returns an array of all person records in the address book database that are linked to the given person record.
- [func ABPersonCopyCompositeNameDelimiterForRecord(ABRecord!) -> Unmanaged<CFString>!](abpersoncopycompositenamedelimiterforrecord(_:).md)
  Returns the delimiter to use between name components.
- [func ABPersonCopyImageDataWithFormat(ABRecord!, ABPersonImageFormat) -> Unmanaged<CFData>!](abpersoncopyimagedatawithformat(_:_:).md)
  Returns the picture for a person record in the given format.
- [func ABPersonCopyLocalizedPropertyName(ABPropertyID) -> Unmanaged<CFString>!](abpersoncopylocalizedpropertyname(_:).md)
  Returns the localized name of a person property
- [func ABPersonCopySource(ABRecord!) -> Unmanaged<ABRecord>!](abpersoncopysource(_:).md)
  Returns the source that the person record is from.
- [func ABPersonCreateInSource(ABRecord!) -> Unmanaged<ABRecord>!](abpersoncreateinsource(_:).md)
  Creates a new person record in a particular source.
- [func ABPersonCreatePeopleInSourceWithVCardRepresentation(ABRecord!, CFData!) -> Unmanaged<CFArray>!](abpersoncreatepeopleinsourcewithvcardrepresentation(_:_:).md)
  Creates person records from the given vCard representation.
- [func ABPersonCreateVCardRepresentationWithPeople(CFArray!) -> Unmanaged<CFData>!](abpersoncreatevcardrepresentationwithpeople(_:).md)
  Returns the vCard representation of the given person records.
- [func ABPersonGetCompositeNameFormat() -> ABPersonCompositeNameFormat](abpersongetcompositenameformat().md)
  Returns the person-name display format.
- [func ABPersonGetCompositeNameFormatForRecord(ABRecord!) -> ABPersonCompositeNameFormat](abpersongetcompositenameformatforrecord(_:).md)
  Returns the person-name display format to use for the given record.
- [func ABPersonGetSortOrdering() -> ABPersonSortOrdering](abpersongetsortordering().md)
  Returns the user’s sort-ordering preference for lists of persons.
- [func ABPersonGetTypeOfProperty(ABPropertyID) -> ABPropertyType](abpersongettypeofproperty(_:).md)
  Returns the type of a person property.
- [func ABPersonHasImageData(ABRecord!) -> Bool](abpersonhasimagedata(_:).md)
  Indicates whether a person has a picture.
- [func ABPersonRemoveImageData(ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abpersonremoveimagedata(_:_:).md)
  Removes a person’s picture.
- [func ABRecordCopyCompositeName(ABRecord!) -> Unmanaged<CFString>!](abrecordcopycompositename(_:).md)
  Returns an appropriate, human-friendly name for the record.
- [func ABRecordGetRecordID(ABRecord!) -> ABRecordID](abrecordgetrecordid(_:).md)
  Returns the unique ID of a record.
- [func ABRecordGetRecordType(ABRecord!) -> ABRecordType](abrecordgetrecordtype(_:).md)
  Returns the type of a record.

## See Also

- [C Types](c-types.md)
  Identify the C types that correspond to Address Book objects.
- [Address Book Constants](address-book-constants.md)
  Get the constants you use to specify Address Book information.
- [AddressBook Enumerations](addressbook-enumerations.md)
  Get the enumerations you use to specify Address Book information.
- [AddressBook Data Types](addressbook-data-types.md)
  Get the data types you use to specify Address Book information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/addressbook-functions)*