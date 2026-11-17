# ABPersonView

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

An object that provides a view for displaying and editing contacts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class ABPersonView
```

```objc
@interface ABPersonView : NSView
```

## Overview

> **Note**:  You should not override the [`fieldEditor(_:for:)`](../AppKit/nswindow/fieldeditor%28_,for%29.md) method of the window that contains this view.

## Topics

### Working with Person Views
- [var editing: Bool](./abpersonview/editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var person: ABPerson!](./abpersonview/person.md)
  The contact record being displayed.
- [var shouldShowLinkedPeople: Bool](./abpersonview/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)

## See Also

### Pickers
- [class ABPeoplePickerView](./abpeoplepickerview.md)
  An object you use to customize the behavior of people-picker views in an app’s user interface.
- [ABPersonPicker](./abpersonpicker.md)
  A picker object that you display when you want the user to select contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview)*