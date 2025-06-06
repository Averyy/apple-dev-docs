# contactPicker(_:didSelectContactProperties:)

**Framework**: Contacts UI  
**Kind**: method

Called after contact properties have been selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contactPicker(_ picker: CNContactPickerViewController, didSelectContactProperties contactProperties: [CNContactProperty])
```

#### Discussion

This delegate method is invoked when the user selects more than one property. Implementing this method configures the picker for multi-selection.

## Parameters

- `picker`: The contact picker where the selection was made.
- `contactProperties`: The selected contact properties.

## See Also

- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](cncontactpickerdelegate/contactpicker(_:didselect:)-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: CNContactProperty)](cncontactpickerdelegate/contactpicker(_:didselect:)-1xfpt.md)
  Called when a property of the contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](cncontactpickerdelegate/contactpicker(_:didselect:)-5neeo.md)
  Called after contacts have been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/contactpicker(_:didselectcontactproperties:))*