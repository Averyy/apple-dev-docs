# contactPickerWillClose(_:)

**Framework**: Contacts UI  
**Kind**: method

In macOS, called when the contact picker’s popover is about to close.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func contactPickerWillClose(_ picker: CNContactPicker)
```

## Parameters

- `picker`: The contact picker popover to be closed.

## See Also

- [func contactPickerDidCancel(CNContactPickerViewController)](cncontactpickerdelegate/contactpickerdidcancel(_:).md)
  In iOS, called when the user taps Cancel.
- [func contactPickerDidClose(CNContactPicker)](cncontactpickerdelegate/contactpickerdidclose(_:).md)
  In macOS, called when the contact picker’s popover has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpickerwillclose(_:))*