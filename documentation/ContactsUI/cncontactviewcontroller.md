# CNContactViewController

**Framework**: Contacts UI  
**Kind**: class

A view controller that displays a new, unknown, or existing contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class CNContactViewController
```

#### Overview

Present a `CNContactViewController` object when you want to display information about one of the user’s contacts. At creation time, you specify the type of contact you want to display: new, unknown, or existing.

## Topics

### Creating the Contact Viewer
- [convenience init(for: CNContact)](cncontactviewcontroller/init(for:).md)
  Initializes a view controller for an existing contact.
- [convenience init(forContact: CNContact)](cncontactviewcontroller/init(forcontact:).md)
  Initializes a view controller for an existing contact.
- [convenience init(forUnknownContact: CNContact)](cncontactviewcontroller/init(forunknowncontact:).md)
  Initializes a view controller for an unknown contact.
- [convenience init(forNewContact: CNContact?)](cncontactviewcontroller/init(fornewcontact:).md)
  Initializes a view controller for a new contact.
### Handling Interactions with the Interface
- [var delegate: (any CNContactViewControllerDelegate)?](cncontactviewcontroller/delegate.md)
  The delegate to be notified.
- [protocol CNContactViewControllerDelegate](cncontactviewcontrollerdelegate.md)
  Methods you use to respond to user interactions with a contact view controller.
### Required Keys
- [class func descriptorForRequiredKeys() -> any CNKeyDescriptor](cncontactviewcontroller/descriptorforrequiredkeys.md)
  Returns the descriptor for all the keys that must be fetched on the contact before setting it on the view controller.
### Displaying Contact Properties
- [var contact: CNContact](cncontactviewcontroller/contact.md)
  The contact being displayed.
- [var alternateName: String?](cncontactviewcontroller/alternatename.md)
  The name to use if the contact has no display name.
- [var message: String?](cncontactviewcontroller/message.md)
  The message displayed under the name of the contact.
- [var displayedPropertyKeys: [Any]?](cncontactviewcontroller/displayedpropertykeys.md)
  The contact property keys to display.
### Configuring the Contact’s Relationships
- [var parentGroup: CNGroup?](cncontactviewcontroller/parentgroup.md)
  The group in which to add a new contact.
- [var parentContainer: CNContainer?](cncontactviewcontroller/parentcontainer.md)
  The container in which to add a new contact.
### Contact Store
- [var contactStore: CNContactStore?](cncontactviewcontroller/contactstore.md)
  The contact store from which the contact was fetched or to which it will be saved.
### Customizing Contact Card
- [var allowsEditing: Bool](cncontactviewcontroller/allowsediting.md)
  Determines whether the user can edit the contact’s information.
- [var allowsActions: Bool](cncontactviewcontroller/allowsactions.md)
  Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var shouldShowLinkedContacts: Bool](cncontactviewcontroller/shouldshowlinkedcontacts.md)
  Determines whether to display data from contacts that are linked to the contact being displayed.
### Highlighting a Property
- [func highlightProperty(withKey: String, identifier: String?)](cncontactviewcontroller/highlightproperty(withkey:identifier:).md)
  Highlights the property of the contact being displayed.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller)*