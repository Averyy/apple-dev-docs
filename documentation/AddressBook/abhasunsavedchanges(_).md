# ABHasUnsavedChanges(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns whether if there are unsaved changes in the address book.

**Availability**:
- macOS

## Declaration

```swift
func ABHasUnsavedChanges(_ addressBook: ABAddressBookRef!) -> Bool
```

```c
extern bool ABHasUnsavedChanges(ABAddressBookRef addressBook);
```

#### Return Value

`true` if there are unsaved changes, `false` otherwise.

#### Discussion

The unsaved changes flag is set automatically whenever changes are made to the address book.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

### Address Book
- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](./abgetsharedaddressbook%28%29.md)
  Returns the unique shared ABAddressBook object.
- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](./abcopydefaultcountrycode%28_%29.md)
  Returns the default country code for records with unspecified country codes.
- [func ABSave(ABAddressBookRef!) -> Bool](./absave%28_%29.md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abhasunsavedchanges(_:))*