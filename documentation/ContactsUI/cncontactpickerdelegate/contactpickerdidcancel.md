# contactPickerDidCancel(_:)

**Framework**: Contacts UI  
**Kind**: method

In iOS, called when the user taps Cancel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contactPickerDidCancel(_ picker: CNContactPickerViewController)
```

#### Discussion

The picker is dismissed automatically after a contact or property is picked.

## Parameters

- `picker`: The contact picker in which the selection was made.

## See Also

- [func contactPickerWillClose(CNContactPicker)](cncontactpickerdelegate/contactpickerwillclose(_:).md)
  In macOS, called when the contact picker’s popover is about to close.
- [func contactPickerDidClose(CNContactPicker)](cncontactpickerdelegate/contactpickerdidclose(_:).md)
  In macOS, called when the contact picker’s popover has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpickerdidcancel(_:))*