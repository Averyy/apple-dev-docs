# ABExternalChangeCallback

**Framework**: Address Book  
**Kind**: typealias

Prototype for a function callback invoked on an address book when the Address Book database is modified by another address book instance.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias ABExternalChangeCallback = (ABAddressBook?, CFDictionary?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

If you name your callback function `MyAddressBookExternalChangeCallback`, you declare it like this:

##### Discussion

Use [`ABAddressBookRegisterExternalChangeCallback(_:_:_:)`](abaddressbookregisterexternalchangecallback(_:_:_:).md) to register and [`ABAddressBookUnregisterExternalChangeCallback(_:_:_:)`](abaddressbookunregisterexternalchangecallback(_:_:_:).md) to unregister the callback function.

You can register for a callback with different contexts or callback functions. The run loop on the thread that registered the callback invokes the callback.

The `addressBook` object does not take any action to flush or synchronize cached state with the Address Book database. If you want to ensure that `addressBook` doesn’t contain stale values, use [`ABAddressBookRevert(_:)`](abaddressbookrevert(_:).md).

## Parameters

- `addressBook`: An address book used to interact with the Address Book database.
- `info`: Always  .
- `context`: The object to pass to the callback function.

## See Also

- [typealias ABAddressBookRequestAccessCompletionHandler](abaddressbookrequestaccesscompletionhandler.md)
  Definition for a block callback invoked when an access request has completed.
- [typealias ABMultiValueIdentifier](abmultivalueidentifier.md)
  Identifies multivalue properties.
- [typealias ABPersonCompositeNameFormat](abpersoncompositenameformat.md)
  Indicates a person-name display format.
- [typealias ABPersonSortOrdering](abpersonsortordering.md)
  Indicates a person sort ordering.
- [typealias ABPropertyID](abpropertyid.md)
  Integer that identifies a record property.
- [typealias ABRecordID](abrecordid.md)
  Integer that identifies a record.
- [typealias ABRecordType](abrecordtype.md)
  Integer that identifies a record type.
- [typealias ABSourceType](absourcetype.md)
  Indicates a source type. See `Source Properties`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abexternalchangecallback)*