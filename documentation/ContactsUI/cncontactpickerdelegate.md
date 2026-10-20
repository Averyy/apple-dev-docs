# CNContactPickerDelegate

**Framework**: Contacts UI  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CNContactPickerDelegate <NSObject>
```

## Topics

### Responding to User Selections
- [func contactPicker(CNContactPickerViewController, didSelect: CNContact)](./cncontactpickerdelegate/contactpicker%28_,didselect%29-7vcyc.md)
  Called after a contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: CNContactProperty)](./cncontactpickerdelegate/contactpicker%28_,didselect%29-1xfpt.md)
  Called when a property of the contact has been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelect: [CNContact])](./cncontactpickerdelegate/contactpicker%28_,didselect%29-5neeo.md)
  Called after contacts have been selected by the user.
- [func contactPicker(CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](./cncontactpickerdelegate/contactpicker%28_,didselectcontactproperties%29.md)
  Called after contact properties have been selected by the user.
### Dismissing the Picker Interface
- [func contactPickerDidCancel(CNContactPickerViewController)](./cncontactpickerdelegate/contactpickerdidcancel%28_%29.md)
  In iOS, called when the user taps Cancel.
- [func contactPickerWillClose(CNContactPicker)](./cncontactpickerdelegate/contactpickerwillclose%28_%29.md)
  In macOS, called when the contact picker’s popover is about to close.
- [func contactPickerDidClose(CNContactPicker)](./cncontactpickerdelegate/contactpickerdidclose%28_%29.md)
  In macOS, called when the contact picker’s popover has closed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [var delegate: (any CNContactPickerDelegate)?](./cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.
- [var delegate: (any CNContactPickerDelegate)?](./cncontactpickerviewcontroller/delegate.md)
  The delegate to be notified when the user selects a contact or a property.
### Responding to Picker Interactions
- [var delegate: (any CNContactPickerDelegate)?](./cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate)*