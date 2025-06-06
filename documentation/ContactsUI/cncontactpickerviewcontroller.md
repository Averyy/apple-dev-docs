# CNContactPickerViewController

**Framework**: Contacts UI  
**Kind**: class

A view controller that displays an interface for picking contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class CNContactPickerViewController
```

#### Overview

A [`CNContactPickerViewController`](cncontactpickerviewcontroller.md) allows the user to select one or more contacts (or their properties) from the list of contacts displayed in the contact view controller ([`CNContactViewController`](cncontactviewcontroller.md)). The picker supports both single selection and multiselection of the contacts. The app using contact picker view does not need access to the user’s contacts and the user will not be prompted for “grant permission” access. The app has access only to the user’s final selection.

There are predefined predicates in this class that let you control the user selection of the contact. Changing the predicates only take effect before the view is presented.

## Topics

### Displaying Contacts Properties
- [var displayedPropertyKeys: [String]?](cncontactpickerviewcontroller/displayedpropertykeys.md)
  The [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) property keys to display in the contact detail card.
### Responding to User Interactions
- [var delegate: (any CNContactPickerDelegate)?](cncontactpickerviewcontroller/delegate.md)
  The delegate to be notified when the user selects a contact or a property.
- [protocol CNContactPickerDelegate](cncontactpickerdelegate.md)
  The methods that you implement to respond to contact-picker user events.
### Predicates For Selecting Contacts
- [var predicateForEnablingContact: NSPredicate?](cncontactpickerviewcontroller/predicateforenablingcontact.md)
  A predicate to determine the contact selectability in the list of contacts.
- [var predicateForSelectionOfContact: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofcontact.md)
  A predicate to control the return of the selected contact.
- [var predicateForSelectionOfProperty: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofproperty.md)
  A predicate to control the properties of the selected contact.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class CNContactPicker](cncontactpicker.md)
  A popover-based interface for selecting a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller)*