# NSPanel

**Framework**: AppKit  
**Kind**: class

A special kind of window that typically performs a function that is auxiliary to the main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPanel
```

#### Overview

For details about how panels work (especially to find out how their behavior differs from window behavior), see [`How Panels Work`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingPanels.html#//apple_ref/doc/uid/20000224).

## Topics

### Configuring Panels
- [var isFloatingPanel: Bool](nspanel/isfloatingpanel.md)
  A Boolean value that indicates whether the receiver is a floating panel.
- [var becomesKeyOnlyIfNeeded: Bool](nspanel/becomeskeyonlyifneeded.md)
  A Boolean value that indicates whether the receiver becomes the key window only when needed.
- [var worksWhenModal: Bool](nspanel/workswhenmodal.md)
  A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.
### Constants
- [Alert Panel Return Values](alert-panel-return-values.md)
  These constants define values returned by the [`NSRunAlertPanel`](nsrunalertpanel.md) function and by the `NSApplication` method [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) when the modal session is run with an `NSPanel` provided by the [`NSGetAlertPanel`](nsgetalertpanel.md) function.
- [Modal Panel Return Values](modal-panel-return-values.md)
  These constants define the possible return values for such methods as the `runModal...` methods of the [`NSOpenPanel`](nsopenpanel.md) class, which tell which button (OK or Cancel) the user has clicked on an open panel.
- [Style Masks](style-masks.md)
  Constants that specify panel styles.

## Relationships

### Inherits From
- [NSWindow](nswindow.md)
### Inherited By
- [NSColorPanel](nscolorpanel.md)
- [NSFontPanel](nsfontpanel.md)
- [NSSavePanel](nssavepanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
- [class NSWindowTab](nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.
- [class NSWindowTabGroup](nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel)*