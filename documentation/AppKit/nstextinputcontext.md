# NSTextInputContext

**Framework**: AppKit  
**Kind**: class

An object that represents the Cocoa text input system.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class NSTextInputContext
```

#### Overview

The text input system communicates primarily with the client of the activated input context via the [`NSTextInputClient`](nstextinputclient.md) protocol.

## Topics

### Creating an Input Context
- [init(client: any NSTextInputClient)](nstextinputcontext/init(client:).md)
  The designated initializer
### Getting the Input Context and Client
- [class var current: NSTextInputContext?](nstextinputcontext/current.md)
  Returns the current, activated, text input context object.
- [var client: any NSTextInputClient](nstextinputcontext/client.md)
  The owner of this input context. (read-only)
### Configuring the Input Context
- [var acceptsGlyphInfo: Bool](nstextinputcontext/acceptsglyphinfo.md)
  A Boolean value that indicates whether the client handles `NSGlyphInfoAttributeName` or not.
- [var allowedInputSourceLocales: [String]?](nstextinputcontext/allowedinputsourcelocales.md)
  The set of keyboard input source locales allowed when this input context is active.
### Activating the Input Context
- [func activate()](nstextinputcontext/activate.md)
  Activates the receiver.
- [func deactivate()](nstextinputcontext/deactivate.md)
  Deactivates the receiver.
### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](nstextinputcontext/handleevent(_:).md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](nstextinputcontext/discardmarkedtext.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [func invalidateCharacterCoordinates()](nstextinputcontext/invalidatecharactercoordinates.md)
  Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](nstextinputcontext/keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](nstextinputcontext/selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](nstextinputcontext/localizedname(forinputsource:).md)
  Returns the display name for the given text input source identifier.
- [typealias NSTextInputSourceIdentifier](nstextinputsourceidentifier.md)
### Notifications
- [class let keyboardSelectionDidChangeNotification: NSNotification.Name](nstextinputcontext/keyboardselectiondidchangenotification.md)
  Posted after the selected text input source changes.
### Instance Methods
- [func textInputClientDidEndScrollingOrZooming()](nstextinputcontext/textinputclientdidendscrollingorzooming.md)
- [func textInputClientWillStartScrollingOrZooming()](nstextinputcontext/textinputclientwillstartscrollingorzooming.md)
- [func textInputClientDidScroll()](nstextinputcontext/textinputclientdidscroll.md)
- [func textInputClientDidUpdateSelection()](nstextinputcontext/textinputclientdidupdateselection.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext)*