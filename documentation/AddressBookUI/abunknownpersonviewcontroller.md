# ABUnknownPersonViewController

**Framework**: Address Book UI  
**Kind**: class

The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ABUnknownPersonViewController
```

#### Overview

Unknown-person view controllers display contact information that can be saved to the Address Book database. From instances of this class, users may also initiate standard actions, such as:

- Phone call
- Text message
- Create contact
- Add to contact

Performing any of the standard actions may result in your application being moved to the background.

> ❗ **Important**:  Unknown-person view controllers must be used with a navigation controller in order to function properly.

##### Subclassing

The `ABUnknownPersonViewController` class does not support subclassing.

## Topics

### Responding to View Controller Interactions
- [var unknownPersonViewDelegate: (any ABUnknownPersonViewControllerDelegate)?](abunknownpersonviewcontroller/unknownpersonviewdelegate.md)
  The unknown-person view controller delegate.
- [protocol ABUnknownPersonViewControllerDelegate](abunknownpersonviewcontrollerdelegate.md)
  The methods you use to respond to events in an unknown person view controller.
### Displaying Person Properties
- [var alternateName: String?](abunknownpersonviewcontroller/alternatename.md)
  Provides a value that is displayed instead of the first and last name.
- [var message: String?](abunknownpersonviewcontroller/message.md)
  Text displayed below [`alternateName`](abunknownpersonviewcontroller/alternatename.md).
- [var displayedPerson: ABRecord](abunknownpersonviewcontroller/displayedperson.md)
  Specifies a person record whose properties are displayed by the view controller.
### Configuring the Interface Details
- [var addressBook: ABAddressBook?](abunknownpersonviewcontroller/addressbook.md)
  Optional. The address book database that the person record is added to.
- [var allowsActions: Bool](abunknownpersonviewcontroller/allowsactions.md)
  Specifies whether buttons appear to let the user perform actions such as sharing the contact, initiating a FaceTime call, or sending a text message.
- [var allowsAddingToAddressBook: Bool](abunknownpersonviewcontroller/allowsaddingtoaddressbook.md)
  Specifies whether the user can add the properties displayed by the unknown-person view controller to the address book database, either as a new contact or by adding them to an existing contact.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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

- [class ABNewPersonViewController](abnewpersonviewcontroller.md)
  A view controller presenting an interface to create a contact.
- [class ABPersonViewController](abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](abcreatestringwithaddressdictionary(_:_:).md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller)*