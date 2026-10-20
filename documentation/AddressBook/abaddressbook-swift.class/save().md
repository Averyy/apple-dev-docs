# save()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Saves all the changes made since the last save.

**Availability**:
- macOS

## Declaration

```swift
func save() -> Bool
```

```objc
- (BOOL) save;
```

#### Return Value

[`true`](../../Swift/true.md) if successful or there were no changes; otherwise, [`false`](../../Swift/false.md).

## See Also

### Saving and Detecting Changes
- [func hasUnsavedChanges() -> Bool](./hasunsavedchanges%28%29.md)
  Indicates whether an address book has changes that have not been saved to the Address Book database.
- [func saveAndReturnError() throws](./saveandreturnerror%28%29.md)
  Saves all the changes made since the last save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/save())*