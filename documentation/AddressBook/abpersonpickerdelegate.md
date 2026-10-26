# ABPersonPickerDelegate

**Framework**: Address Book  
**Kind**: protocol  
**Role**: Protocol

Methods you use to respond to user selections in a person picker.

**Availability**:
- macOS 10.9+

## Declaration

```objc
@protocol ABPersonPickerDelegate <NSObject>
```

## Topics

### Handling Selections
- [- personPicker:didChoosePerson:property:identifier:](./abpersonpickerdelegate/personpicker_didchooseperson_property_identifier_.md)
  Informs the delegate when the user selects a person, or a specific property of a person.
- [- personPickerDidClose:](./abpersonpickerdelegate/personpickerdidclose_.md)
  Notifies the delegate when the user closes the  picker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing the Picker Interface
- [delegate](./abpersonpicker/delegate.md)
  An object the system notifies as the user interacts with the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonpickerdelegate)*