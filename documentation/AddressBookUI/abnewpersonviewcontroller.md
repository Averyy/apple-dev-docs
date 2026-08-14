# ABNewPersonViewController

**Framework**: Address Book UI  
**Kind**: class

A view controller presenting an interface to create a contact.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ABNewPersonViewController
```

#### Overview

New-person view controllers are modal view controllers that manage a set of view controllers used to create a contact (`ABPersonRef`) and edit its properties.

> ❗ **Important**:  New-person view controllers must be used with a navigation controller in order to function properly.  It is recommended that you present a new-person view controller modally.

##### Subclassing

The `ABNewPersonViewController` class does not support subclassing.

## Topics

### Responding to View Controller Interactions
- [var newPersonViewDelegate: (any ABNewPersonViewControllerDelegate)?](abnewpersonviewcontroller/newpersonviewdelegate.md)
  The delegate of a new-person view controller.
- [protocol ABNewPersonViewControllerDelegate](abnewpersonviewcontrollerdelegate.md)
  The `ABNewPersonViewControllerDelegate` protocol declares the interface that [`ABNewPersonViewController`](abnewpersonviewcontroller.md) delegates must implement.
### Displaying Person Properties
- [var displayedPerson: ABRecord?](abnewpersonviewcontroller/displayedperson.md)
  Optional. Specifies the person properties that the new-person view controller pre-fills in its views.
### Configuring New Person Views
- [var addressBook: ABAddressBook?](abnewpersonviewcontroller/addressbook.md)
  Optional. The address book to which the new contact is added.
- [var parentGroup: ABRecord?](abnewpersonviewcontroller/parentgroup.md)
  Optional. Specifies the group to which to add the new contact on save.

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

- [class ABPersonViewController](abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](abcreatestringwithaddressdictionary(_:_:).md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)*