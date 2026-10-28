# discardMarkedText()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the Cocoa text input system to discard the current conversion session.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func discardMarkedText()
```

```objc
- (void) discardMarkedText;
```

## Discussion

The client should clear its marked range when sending this message.

## See Also

### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](./handleevent%28_%29.md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func invalidateCharacterCoordinates()](./invalidatecharactercoordinates%28%29.md)
  Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](./keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](./selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](./localizedname%28forinputsource%29.md)
  Returns the display name for the given text input source identifier.
- [typealias NSTextInputSourceIdentifier](../nstextinputsourceidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/discardmarkedtext())*