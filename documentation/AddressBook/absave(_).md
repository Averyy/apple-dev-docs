# ABSave(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Saves all the changes made since the last save.

**Availability**:
- macOS

## Declaration

```swift
func ABSave(_ addressBook: ABAddressBookRef!) -> Bool
```

```c
extern bool ABSave(ABAddressBookRef addressBook);
```

#### Return Value

`true` if this function is successful or if there were no changes, `false` otherwise.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

### Address Book
- [func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](./abgetsharedaddressbook%28%29.md)
  Returns the unique shared ABAddressBook object.
- [func ABCopyDefaultCountryCode(ABAddressBookRef!) -> Unmanaged<CFString>!](./abcopydefaultcountrycode%28_%29.md)
  Returns the default country code for records with unspecified country codes.
- [func ABHasUnsavedChanges(ABAddressBookRef!) -> Bool](./abhasunsavedchanges%28_%29.md)
  Returns whether if there are unsaved changes in the address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absave(_:))*