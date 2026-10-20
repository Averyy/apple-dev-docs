# ABNewPersonViewController

**Framework**: Address Book UI  
**Kind**: class  
**Role**: Class

A view controller presenting an interface to create a contact.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
class ABNewPersonViewController
```

```objc
@interface ABNewPersonViewController : UIViewController
```

#### Overview

New-person view controllers are modal view controllers that manage a set of view controllers used to create a contact (`ABPersonRef`) and edit its properties.

> ❗ **Important**:  New-person view controllers must be used with a navigation controller in order to function properly.  It is recommended that you present a new-person view controller modally.

##### Subclassing

The `ABNewPersonViewController` class does not support subclassing.

## Topics

### Responding to View Controller Interactions
- [var newPersonViewDelegate: (any ABNewPersonViewControllerDelegate)?](./abnewpersonviewcontroller/newpersonviewdelegate.md)
  The delegate of a new-person view controller.
- [protocol ABNewPersonViewControllerDelegate](./abnewpersonviewcontrollerdelegate.md)
  The `ABNewPersonViewControllerDelegate` protocol declares the interface that [`ABNewPersonViewController`](./abnewpersonviewcontroller.md) delegates must implement.
### Displaying Person Properties
- [var displayedPerson: ABRecord?](./abnewpersonviewcontroller/displayedperson.md)
  Optional. Specifies the person properties that the new-person view controller pre-fills in its views.
### Configuring New Person Views
- [var addressBook: ABAddressBook?](./abnewpersonviewcontroller/addressbook.md)
  Optional. The address book to which the new contact is added.
- [var parentGroup: ABRecord?](./abnewpersonviewcontroller/parentgroup.md)
  Optional. Specifies the group to which to add the new contact on save.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Detail Display
- [class ABPersonViewController](./abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](./abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](./abcreatestringwithaddressdictionary%28_,_%29.md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)*