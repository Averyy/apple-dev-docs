# contactPicker(_:didSelect:)

**Framework**: Contacts UI  
**Kind**: method

Called after contacts have been selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contactPicker(_ picker: CNContactPickerViewController, didSelect contacts: [CNContact])
```

#### Discussion

This delegate method is called when the user selects more than one contact. Implementing this method configures the picker for multi-selection.

## Parameters

- `picker`: The contact picker where the selection was made.
- `contacts`: The selected contacts.

## See Also

- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](cncontactpickerdelegate/contactpicker(_:didselect:)-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: CNContactProperty)](cncontactpickerdelegate/contactpicker(_:didselect:)-1xfpt.md)
  Called when a property of the contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](cncontactpickerdelegate/contactpicker(_:didselectcontactproperties:).md)
  Called after contact properties have been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpicker(_:didselect:)-5neeo)*