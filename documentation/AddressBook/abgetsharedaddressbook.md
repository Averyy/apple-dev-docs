# ABGetSharedAddressBook()

**Framework**: Address Book  
**Kind**: func

Returns the unique shared ABAddressBook object.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!
```

#### Return Value

The address book for the logged-in user. You are responsible for retaining and releasing this object as needed.

#### Discussion

Every application shares the address book for the logged-in user and this function returns it. If you call this function more than once or try to create a new address book, you get a pointer to the same shared address book.

## See Also

- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](abcopydefaultcountrycode(_:).md)
  Returns the default country code for records with unspecified country codes.
- [func ABHasUnsavedChanges(ABAddressBookRef!) -> Bool](abhasunsavedchanges(_:).md)
  Returns whether if there are unsaved changes in the address book.
- [func ABSave(ABAddressBookRef!) -> Bool](absave(_:).md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgetsharedaddressbook())*