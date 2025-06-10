# hasUnsavedChanges()

**Framework**: Address Book  
**Kind**: method

Indicates whether an address book has changes that have not been saved to the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
func hasUnsavedChanges() -> Bool
```

#### Return Value

`true` if there are unsaved changes; otherwise, `false`.

#### Discussion

The unsaved changes flag is set automatically whenever changes are made.

## See Also

- [func save() -> Bool](abaddressbook/save.md)
  Saves all the changes made since the last save.
- [func saveAndReturnError() throws](abaddressbook/saveandreturnerror.md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/hasunsavedchanges())*