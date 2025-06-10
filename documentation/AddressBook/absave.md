# ABSave(_:)

**Framework**: Address Book  
**Kind**: func

Saves all the changes made since the last save.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABSave(_ addressBook: ABAddressBookRef!) -> Bool
```

#### Return Value

`true` if this function is successful or if there were no changes, `false` otherwise.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](abgetsharedaddressbook().md)
  Returns the unique shared ABAddressBook object.
- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](abcopydefaultcountrycode(_:).md)
  Returns the default country code for records with unspecified country codes.
- [func ABHasUnsavedChanges(ABAddressBookRef!) -> Bool](abhasunsavedchanges(_:).md)
  Returns whether if there are unsaved changes in the address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absave(_:))*