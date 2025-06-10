# NSTextInsertionIndicator

**Framework**: AppKit  
**Kind**: class

A view that represents the insertion indicator in text.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
class NSTextInsertionIndicator
```

## Mentions

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)

#### Overview

[`NSTextView`](nstextview.md) and [`NSTextField`](nstextfield.md) both use [`NSTextInsertionIndicator`](nstextinsertionindicator.md) to display the insertion indicator. You can use this indicator if you have your own text engine or need to display an indicator elsewhere.

To use the indicator, instantiate an [`NSTextInsertionIndicator`](nstextinsertionindicator.md), then add the view to your view hierarchy. Set the indicator view’s frame to where you want to display a text insertion indicator. The indicator has the same height as the indicator view’s frame, and centers horizontally within the indicator view’s frame.

The [`NSTextInsertionIndicator.DisplayMode`](nstextinsertionindicator/displaymode-swift.enum.md) specifies whether the indicator hides, remains visible, or blinks (automatic).

When set to [`NSTextInsertionIndicator.DisplayMode.automatic`](nstextinsertionindicator/displaymode-swift.enum/automatic.md), the indicator stops blinking when you set the frame. The indicator starts blinking when the frame doesn’t change for a period of time. When the user dictates, the indicator displays a trailing glow when it is moved.

Set the [`NSTextInsertionIndicator.DisplayMode`](nstextinsertionindicator/displaymode-swift.enum.md) to [`NSTextInsertionIndicator.DisplayMode.automatic`](nstextinsertionindicator/displaymode-swift.enum/automatic.md) when your custom view becomes the first responder. When your custom view resigns first responder, set the [`displayMode`](nstextinsertionindicator/displaymode-swift.property.md) to [`NSTextInsertionIndicator.DisplayMode.hidden`](nstextinsertionindicator/displaymode-swift.enum/hidden.md) to indicate that key events aren’t sent to your view.

By default the indicator’s color is [`textInsertionPointColor`](nscolor/textinsertionpointcolor.md). You can set a different color.

## Topics

### Configuring indicators
- [var color: NSColor!](nstextinsertionindicator/color.md)
  The color of this indicator.
- [var effectsViewInserter: ((NSView) -> Void)?](nstextinsertionindicator/effectsviewinserter.md)
  An optional closure the system calls during dictation.
### Setting the display mode
- [var displayMode: NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.property.md)
  A value that describes the display mode of an indicator.
- [var automaticModeOptions: NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.property.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.

## Relationships

### Inherits From
- [NSView](nsview.md)
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
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator)*