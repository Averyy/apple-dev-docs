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
@MainActor
class ABNewPersonViewController
```

#### Overview

New-person view controllers are modal view controllers that manage a set of view controllers used to create a contact (`ABPersonRef`) and edit its properties.

> ❗ **Important**:  New-person view controllers must be used with a navigation controller in order to function properly.  It is recommended that you present a new-person view controller modally.

 New-person view controllers must be used with a navigation controller in order to function properly.  It is recommended that you present a new-person view controller modally.

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

- [class ABPersonViewController](abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as ) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as ) implements a view controller used to create a person record from a set of person properties.
- [func ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String](abcreatestringwithaddressdictionary(_:_:).md)
  Returns a formatted address from an address property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)*