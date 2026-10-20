# invalidateCharacterCoordinates()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func invalidateCharacterCoordinates()
```

```objc
- (void) invalidateCharacterCoordinates;
```

## See Also

### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](./handleevent%28_%29.md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](./discardmarkedtext%28%29.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](./keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](./selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](./localizedname%28forinputsource%29.md)
  Returns the display name for the given text input source identifier.
- [typealias NSTextInputSourceIdentifier](../nstextinputsourceidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/invalidatecharactercoordinates())*