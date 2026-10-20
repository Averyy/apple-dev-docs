# NSTextInputSourceIdentifier

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias NSTextInputSourceIdentifier = String
```

```c
typedef NSString * NSTextInputSourceIdentifier;
```

## See Also

### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](./nstextinputcontext/handleevent%28_%29.md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](./nstextinputcontext/discardmarkedtext%28%29.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [func invalidateCharacterCoordinates()](./nstextinputcontext/invalidatecharactercoordinates%28%29.md)
  Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](./nstextinputcontext/keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](./nstextinputcontext/selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](./nstextinputcontext/localizedname%28forinputsource%29.md)
  Returns the display name for the given text input source identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputsourceidentifier)*