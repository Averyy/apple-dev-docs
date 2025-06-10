# ABPersonView

**Framework**: Address Book  
**Kind**: class

An object that provides a view for displaying and editing contacts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class ABPersonView
```

#### Overview

> **Note**:  You should not override the [`fieldEditor(_:for:)`](https://developer.apple.com/documentation/AppKit/NSWindow/fieldEditor(_:for:)) method of the window that contains this view.

## Topics

### Working with Person Views
- [var editing: Bool](abpersonview/editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var person: ABPerson!](abpersonview/person.md)
  The contact record being displayed.
- [var shouldShowLinkedPeople: Bool](abpersonview/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ABPeoplePickerView](abpeoplepickerview.md)
  An object you use to customize the behavior of people-picker views in an app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview)*