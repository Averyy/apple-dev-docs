# ABCopyDefaultCountryCode(_:)

**Framework**: Address Book  
**Kind**: func

Returns the default country code for records with unspecified country codes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func ABCopyDefaultCountryCode(_ addressBook: ABAddressBookRef!) -> Unmanaged<CFString>!
```

#### Return Value

A string with the default country code. You are responsible for releasing this object.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](abgetsharedaddressbook().md)
  Returns the unique shared ABAddressBook object.
- [func ABHasUnsavedChanges(ABAddressBookRef!) -> Bool](abhasunsavedchanges(_:).md)
  Returns whether if there are unsaved changes in the address book.
- [func ABSave(ABAddressBookRef!) -> Bool](absave(_:).md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopydefaultcountrycode(_:))*