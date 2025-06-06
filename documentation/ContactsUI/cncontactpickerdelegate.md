# CNContactPickerDelegate

**Framework**: Contacts UI  
**Kind**: protocol

The methods that you implement to respond to contact-picker user events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
protocol CNContactPickerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Selections
- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](cncontactpickerdelegate/contactpicker(_:didselect:)-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: CNContactProperty)](cncontactpickerdelegate/contactpicker(_:didselect:)-1xfpt.md)
  Called when a property of the contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](cncontactpickerdelegate/contactpicker(_:didselect:)-5neeo.md)
  Called after contacts have been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](cncontactpickerdelegate/contactpicker(_:didselectcontactproperties:).md)
  Called after contact properties have been selected by the user.
### Dismissing the Picker Interface
- [func contactPickerDidCancel(CNContactPickerViewController)](cncontactpickerdelegate/contactpickerdidcancel(_:).md)
  In iOS, called when the user taps Cancel.
- [func contactPickerWillClose(CNContactPicker)](cncontactpickerdelegate/contactpickerwillclose(_:).md)
  In macOS, called when the contact picker’s popover is about to close.
- [func contactPickerDidClose(CNContactPicker)](cncontactpickerdelegate/contactpickerdidclose(_:).md)
  In macOS, called when the contact picker’s popover has closed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CNContactPickerDelegate)?](cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.
- [var delegate: (any CNContactPickerDelegate)?](cncontactpickerviewcontroller/delegate.md)
  The delegate to be notified when the user selects a contact or a property.
- [var delegate: (any CNContactPickerDelegate)?](cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate)*