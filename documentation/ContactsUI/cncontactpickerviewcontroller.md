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
class CNContactPickerViewController
```

#### Overview

A [`CNContactPickerViewController`](cncontactpickerviewcontroller.md) allows the user to select one or more contacts (or their properties) from the list of contacts displayed in the contact view controller ([`CNContactViewController`](cncontactviewcontroller.md)). The picker supports both single selection and multiselection of the contacts. The app using contact picker view does not need access to the user’s contacts and the user will not be prompted for “grant permission” access. The app has access only to the user’s final selection.

There are predefined predicates in this class that let you control the user selection of the contact. Changing the predicates only take effect before the view is presented.

## Topics

### Displaying Contacts Properties
- [var displayedPropertyKeys: [String]?](cncontactpickerviewcontroller/displayedpropertykeys.md)
  The [`CNContact`](https://developer.apple.com/documentation/contacts/cncontact) property keys to display in the contact detail card.
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
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class CNContactPicker](cncontactpicker.md)
  A popover-based interface for selecting a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller)*