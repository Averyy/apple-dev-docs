# invalidateCharacterCoordinates()

**Framework**: AppKit  
**Kind**: method

Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func invalidateCharacterCoordinates()
```

## See Also

- [func handleEvent(NSEvent) -> Bool](nstextinputcontext/handleevent(_:).md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](nstextinputcontext/discardmarkedtext.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](nstextinputcontext/keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](nstextinputcontext/selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](nstextinputcontext/localizedname(forinputsource:).md)
  Returns the display name for the given text input source identifier.
- [typealias NSTextInputSourceIdentifier](nstextinputsourceidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/invalidatecharactercoordinates())*