# hasUnsavedChanges()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Indicates whether an address book has changes that have not been saved to the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
func hasUnsavedChanges() -> Bool
```

```objc
- (BOOL) hasUnsavedChanges;
```

#### Return Value

`true` if there are unsaved changes; otherwise, `false`.

#### Discussion

The unsaved changes flag is set automatically whenever changes are made.

## See Also

### Saving and Detecting Changes
- [func save() -> Bool](./save%28%29.md)
  Saves all the changes made since the last save.
- [func saveAndReturnError() throws](./saveandreturnerror%28%29.md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/hasunsavedchanges())*