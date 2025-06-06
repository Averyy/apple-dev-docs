# NSFontPanel

**Framework**: AppKit  
**Kind**: class

The Font panel—a user interface object that displays a list of available fonts, letting the user preview them and change the font used to display text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSFontPanel
```

#### Overview

Actual changes to the font panel are made through conversion messages sent to the shared [`NSFontManager`](nsfontmanager.md) instance. There’s only one Font panel for each app.

## Topics

### Getting the Font Panel
- [class var shared: NSFontPanel](nsfontpanel/shared.md)
  Returns the single `NSFontPanel` instance for the application, creating it if necessary.
- [class var sharedFontPanelExists: Bool](nsfontpanel/sharedfontpanelexists.md)
  Returns [`true`](https://developer.apple.com/documentation/swift/true) if the shared Font panel has been created, [`false`](https://developer.apple.com/documentation/swift/false) if it hasn’t.
### Enabling Font Changes
- [var isEnabled: Bool](nsfontpanel/isenabled.md)
  A Boolean that shows whether the receiver’s Set button is enabled.
- [func reloadDefaultFontFamilies()](nsfontpanel/reloaddefaultfontfamilies.md)
  Triggers a reload to the default state, so that the delegate is called.
### Updating the Font Panel
- [func setPanelFont(NSFont, isMultiple: Bool)](nsfontpanel/setpanelfont(_:ismultiple:).md)
  Sets the selected font in the receiver to the specified font.
### Converting Fonts
- [func convert(NSFont) -> NSFont](nsfontpanel/convert(_:).md)
  Converts the specified font using the settings in the receiver, with the aid of the shared `NSFontManager` if necessary.
### Working in Modal Loops
- [var worksWhenModal: Bool](nsfontpanel/workswhenmodal.md)
  A Boolean that indicates whether the receiver allows fonts to be changed in modal windows and panels.
### Setting an Accessory View
- [var accessoryView: NSView?](nsfontpanel/accessoryview.md)
  The specified view as the receiver’s accessory view, allowing you to add custom controls to your application’s Font panel without having to create a subclass.
### Structures
- [NSFontPanel.ModeMask](nsfontpanel/modemask.md)

## Relationships

### Inherits From
- [NSPanel](nspanel.md)
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

- [NSFontPanel.ModeMask](nsfontpanel/modemask.md)
- [NSFontPanelValidation](nsfontpanelvalidation.md)
  A set of methods you use to tell the Font panel to display some or all of its elements.
- [protocol NSFontChanging](nsfontchanging.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel)*