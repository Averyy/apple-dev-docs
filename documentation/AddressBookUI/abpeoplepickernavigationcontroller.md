# ABPeoplePickerNavigationController

**Framework**: Address Book UI  
**Kind**: class

The `ABPeoplePickerNavigationController` class (whose instances are known as ) implements a view controller that manages a set of views that allow the user to select a contact or one of its contact-information items from an address book.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class ABPeoplePickerNavigationController
```

#### Overview

In iOS 8 and later bringing up a people-picker navigtion controller does not require the app to have access to a user’s contacts, and the user will not be prompted to grant access. If the app does not itself have access to the user’s contacts, a temporary copy of the contact selected by the user will be returned to the app.

See PeoplePicker: Picking a Person or Property for a sample project illustrating the use of a people-picker navigation controller.

##### Subclassing

The `ABPeoplePickerNavigationController` class does not support subclassing.

## Topics

### Responding to View Controller Interactions
- [var peoplePickerDelegate: (any ABPeoplePickerNavigationControllerDelegate)?](abpeoplepickernavigationcontroller/peoplepickerdelegate.md)
  The people-picker navigation controller delegate.
- [protocol ABPeoplePickerNavigationControllerDelegate](abpeoplepickernavigationcontrollerdelegate.md)
  The `ABPeoplePickerNavigationControllerDelegate` protocol describes the interface [`ABPeoplePickerNavigationController`](abpeoplepickernavigationcontroller.md) delegates must adopt to respond to people-picker user events.
### Displaying Person Properties
- [var displayedProperties: [NSNumber]?](abpeoplepickernavigationcontroller/displayedproperties.md)
  The properties (such as name or telephone number) the picker displays when it shows a person.
### Configuring People Pickers
- [var addressBook: ABAddressBook?](abpeoplepickernavigationcontroller/addressbook.md)
  Optional; the address book from which to obtain the list of contacts.
### Customizing Display and Selection
- [var predicateForEnablingPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforenablingperson.md)
  Optionally determines if a person can be selected.
- [var predicateForSelectionOfPerson: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofperson.md)
  Optionally determines if a selected person should be returned to the app or displayed.
- [var predicateForSelectionOfProperty: NSPredicate?](abpeoplepickernavigationcontroller/predicateforselectionofproperty.md)
  Optionally determines if a selected property should be returned to the app or if the default action for the property should be performed
### Constants
- [Address Book Properties](address-book-properties.md)
  These constants can be used in predicates for selecting people or properties. A labeled value is an object with a “label” property and a “value” property.

## Relationships

### Inherits From
- [UINavigationController](../UIKit/UINavigationController.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)*