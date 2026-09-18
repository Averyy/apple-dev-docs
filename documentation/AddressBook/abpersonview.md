# ABPersonView

**Framework**: Address Book  
**Kind**: class

An object that provides a view for displaying and editing contacts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class ABPersonView
```

#### Overview

> **Note**:  You should not override the [`fieldEditor(_:for:)`](https://developer.apple.com/documentation/appkit/nswindow/fieldeditor(_:for:)) method of the window that contains this view.

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
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## See Also

- [class ABPeoplePickerView](abpeoplepickerview.md)
  An object you use to customize the behavior of people-picker views in an app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview)*