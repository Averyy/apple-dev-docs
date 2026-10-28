# keyboardInputSources

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of keyboard text input source identifier strings available to the receiver. (read-only)

**Availability**:
- macOS 10.6+

## Declaration

```swift
var keyboardInputSources: [NSTextInputSourceIdentifier]? { get }
```

```objc
@property (readonly, nullable) NSArray<NSString *> * keyboardInputSources;
```

## Discussion

The Text Input Source Services API identifies text input sources with text input source identifier strings (for example, `com.apple.inputmethod.Kotoeri.Japanese`) supplied by the underlying text input sources framework. The ID corresponds to the `kTISPropertyInputSourceID` attribute.

For more information on the Text Input Source Services API, see `Text Input Source Services`.

## See Also

### Handling Input Sources
- [func handleEvent(NSEvent) -> Bool](./handleevent%28_%29.md)
  Tells the Cocoa text input system to handle mouse or key events.
- [func discardMarkedText()](./discardmarkedtext%28%29.md)
  Tells the Cocoa text input system to discard the current conversion session.
- [func invalidateCharacterCoordinates()](./invalidatecharactercoordinates%28%29.md)
  Notifies the Cocoa text input system that the position information previously queried via methods like `firstRectForCharacterRange:actualRange:` needs to be updated.
- [var selectedKeyboardInputSource: NSTextInputSourceIdentifier?](./selectedkeyboardinputsource.md)
  The identifier string for the selected keyboard text input source.
- [class func localizedName(forInputSource: NSTextInputSourceIdentifier) -> String?](./localizedname%28forinputsource%29.md)
  Returns the display name for the given text input source identifier.
- [typealias NSTextInputSourceIdentifier](../nstextinputsourceidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/keyboardinputsources)*