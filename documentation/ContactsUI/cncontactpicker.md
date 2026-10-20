# CNContactPicker

**Framework**: Contacts UI  
**Kind**: class  
**Role**: Class

A popover-based interface for selecting a contact.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class CNContactPicker
```

```objc
@interface CNContactPicker : NSObject
```

#### Overview

Before displaying the popover, configure the [`displayedKeys`](./cncontactpicker/displayedkeys.md) property with the information you want to display in the interface.

## Topics

### Responding to Picker Interactions
- [var delegate: (any CNContactPickerDelegate)?](./cncontactpicker/delegate.md)
  The picker delegate to be notified when the user chooses a contact.
- [protocol CNContactPickerDelegate](./cncontactpickerdelegate.md)
  The methods that you implement to respond to contact-picker user events.
### Configuring the Picker Contents
- [var displayedKeys: [String]](./cncontactpicker/displayedkeys.md)
  The keys to be displayed when a contact is expanded.
### Displaying the Popover
- [func showRelative(to: NSRect, of: NSView, preferredEdge: NSRectEdge)](./cncontactpicker/showrelative%28to,of,preferrededge%29.md)
  Shows the picker popover anchored to the specified view.
### Closing the Popover
- [func close()](./cncontactpicker/close%28%29.md)
  Closes the popover.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Contact pickers
- [class CNContactPickerViewController](./cncontactpickerviewcontroller.md)
  A view controller that displays an interface for picking contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpicker)*