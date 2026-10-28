# localizedName(forInputSource:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the display name for the given text input source identifier.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func localizedName(forInputSource inputSourceIdentifier: NSTextInputSourceIdentifier) -> String?
```

```objc
+ (NSString *) localizedNameForInputSource:(NSTextInputSourceIdentifier) inputSourceIdentifier;
```

## Return Value

The localized display name for `inputSourceIdentifier`.

## Parameters

- `inputSourceIdentifier`: The text input source identifier.

## See Also

### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](./handleevent%28_%29.md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](./discardmarkedtext%28%29.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [func invalidateCharacterCoordinates()](./invalidatecharactercoordinates%28%29.md)
  Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.
- [var keyboardInputSources: [NSTextInputSourceIdentifier]?](./keyboardinputsources.md)
  The array of keyboard text input source identifier strings available to the receiver. (read-only)
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](./selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [typealias NSTextInputSourceIdentifier](../nstextinputsourceidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/localizedname(forinputsource:))*