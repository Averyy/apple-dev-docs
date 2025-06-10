# ABHasUnsavedChanges(_:)

**Framework**: Address Book  
**Kind**: func

Returns whether if there are unsaved changes in the address book.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABHasUnsavedChanges(_ addressBook: ABAddressBookRef!) -> Bool
```

#### Return Value

`true` if there are unsaved changes, `false` otherwise.

#### Discussion

The unsaved changes flag is set automatically whenever changes are made to the address book.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](abgetsharedaddressbook().md)
  Returns the unique shared ABAddressBook object.
- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](abcopydefaultcountrycode(_:).md)
  Returns the default country code for records with unspecified country codes.
- [func ABSave(ABAddressBookRef!) -> Bool](absave(_:).md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abhasunsavedchanges(_:))*