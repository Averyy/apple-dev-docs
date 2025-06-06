# CNContactPicker

**Framework**: Contacts UI  
**Kind**: class

A popover-based interface for selecting a contact.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class CNContactPicker
```

#### Overview

Before displaying the popover, configure the [`displayedKeys`](cncontactpicker/displayedkeys.md) property with the information you want to display in the interface.

## Topics

### Responding to Picker Interactions
- [var delegate: (any CNContactPickerDelegate)?](cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.
- [protocol CNContactPickerDelegate](cncontactpickerdelegate.md)
  The methods that you implement to respond to contact-picker user events.
### Configuring the Picker Contents
- [var displayedKeys: [String]](cncontactpicker/displayedkeys.md)
  The keys to be displayed when a contact is expanded.
### Displaying the Popover
- [func showRelative(to: NSRect, of: NSView, preferredEdge: NSRectEdge)](cncontactpicker/showrelative(to:of:preferrededge:).md)
  Shows the picker popover anchored to the specified view.
### Closing the Popover
- [func close()](cncontactpicker/close.md)
  Closes the popover.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CNContactPickerViewController](cncontactpickerviewcontroller.md)
  A view controller that displays an interface for picking contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpicker)*