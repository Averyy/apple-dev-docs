# ABPersonViewController

**Framework**: Address Book UI  
**Kind**: class

The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ABPersonViewController
```

#### Overview

> ❗ **Important**:  Person view controllers must be used with a navigation controller in order to function properly.

##### Subclassing

The `ABPersonViewController` class does not support subclassing.

## Topics

### Responding to View Controller Interactions
- [var personViewDelegate: (any ABPersonViewControllerDelegate)?](abpersonviewcontroller/personviewdelegate.md)
  The person-view controller delegate.
- [protocol ABPersonViewControllerDelegate](abpersonviewcontrollerdelegate.md)
  The `ABPersonViewControllerDelegate` protocol declares the interface that must be implemented by [`ABPersonViewController`](abpersonviewcontroller.md) delegates.
### Displaying Person Properties
- [var displayedPerson: ABRecord](abpersonviewcontroller/displayedperson.md)
  The person displayed by the person view.
- [var displayedProperties: [NSNumber]?](abpersonviewcontroller/displayedproperties.md)
  Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](abpersonviewcontroller/displayedperson.md) the receiver displays.
- [var shouldShowLinkedPeople: Bool](abpersonviewcontroller/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.
### Configuring Person Views
- [var addressBook: ABAddressBook?](abpersonviewcontroller/addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsActions: Bool](abpersonviewcontroller/allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var allowsEditing: Bool](abpersonviewcontroller/allowsediting.md)
  Specifies whether the user can edit the person’s information.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:).md)
  Specifies whether to highlight a particular property of the displayed person.

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
- [UIViewControllerRestoration](../uikit/uiviewcontrollerrestoration.md)

## See Also

- [class ABNewPersonViewController](abnewpersonviewcontroller.md)
  A view controller presenting an interface to create a contact.
- [class ABUnknownPersonViewController](abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](abcreatestringwithaddressdictionary(_:_:).md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller)*