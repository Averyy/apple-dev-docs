# contactPickerWillClose(_:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

In macOS, called when the contact picker’s popover is about to close.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func contactPickerWillClose(_ picker: CNContactPicker)
```

```objc
- (void) contactPickerWillClose:(CNContactPicker *) picker;
```

## Parameters

- `picker`: The contact picker popover to be closed.

## See Also

### Dismissing the Picker Interface
- [func contactPickerDidCancel(CNContactPickerViewController)](./contactpickerdidcancel%28_%29.md)
  In iOS, called when the user taps Cancel.
- [func contactPickerDidClose(CNContactPicker)](./contactpickerdidclose%28_%29.md)
  In macOS, called when the contact picker’s popover has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpickerwillclose(_:))*