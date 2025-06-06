# contactPicker(_:didSelect:)

**Framework**: Contacts UI  
**Kind**: method

Called when a property of the contact has been selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func contactPicker(_ picker: CNContactPicker, didSelect contactProperty: CNContactProperty)
```

#### Discussion

This delegate method ia called when the user selects a single property of the contact.

## Parameters

- `picker`: The contact picker where the selection was made.
- `contactProperty`: The selected contact property.

## See Also

- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](cncontactpickerdelegate/contactpicker(_:didselect:)-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](cncontactpickerdelegate/contactpicker(_:didselect:)-5neeo.md)
  Called after contacts have been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](cncontactpickerdelegate/contactpicker(_:didselectcontactproperties:).md)
  Called after contact properties have been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpicker(_:didselect:)-1xfpt)*