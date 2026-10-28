# handleEvent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the Cocoa text input system to handle mouse or key events.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func handleEvent(_ event: NSEvent) -> Bool
```

```objc
- (BOOL) handleEvent:(NSEvent *) event;
```

## Return Value

[`true`](../../Swift/true.md) if the system consumed the event; otherwise [`false`](../../Swift/false.md).

## Parameters

- `event`: The event to handle.

## See Also

### Handling Input Sources
- [func discardMarkedText()](./discardmarkedtext%28%29.md)
  Tells the Cocoa text input system to discard the current conversion session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/handleevent(_:))*