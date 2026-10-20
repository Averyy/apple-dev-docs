# ABRecord

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

A reference to an ABRecord object or any of its derivedopaque types.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use CNContact, CNGroup, or CNContainer

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
typealias ABRecord = CFTypeRef
```

*macOS*

```swift
typealias ABRecordRef = AnyObject
```

*iOS, iPadOS, Mac Catalyst*

```c
typedef CFTypeRef ABRecordRef;
```

*macOS*

```c
typedef void * ABRecordRef;
```

## See Also

### Deprecated
- [typealias ABAddressBookRequestAccessCompletionHandler](./abaddressbookrequestaccesscompletionhandler.md)
  Definition for a block callback invoked when an access request has completed.
- [typealias ABExternalChangeCallback](./abexternalchangecallback.md)
  Prototype for a function callback invoked on an address book when the Address Book database is modified by another address book instance.
- [typealias ABMultiValueIdentifier](./abmultivalueidentifier.md)
  Identifies multivalue properties.
- [typealias ABPersonCompositeNameFormat](./abpersoncompositenameformat.md)
  Indicates a person-name display format.
- [typealias ABPersonSortOrdering](./abpersonsortordering.md)
  Indicates a person sort ordering.
- [typealias ABPropertyID](./abpropertyid.md)
  Integer that identifies a record property.
- [typealias ABRecordID](./abrecordid.md)
  Integer that identifies a record.
- [typealias ABRecordType](./abrecordtype.md)
  Integer that identifies a record type.
- [typealias ABSourceType](./absourcetype.md)
  Indicates a source type. See `Source Properties`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.typealias)*