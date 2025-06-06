# displayMode

**Framework**: AppKit  
**Kind**: property

A value that describes the display mode of an indicator.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var displayMode: NSTextInsertionIndicator.DisplayMode { get set }
```

#### Discussion

Set the [`displayMode`](nstextinsertionindicator/displaymode-swift.property.md) to [`NSTextInsertionIndicator.DisplayMode.automatic`](nstextinsertionindicator/displaymode-swift.enum/automatic.md) when your custom view becomes the first responder. When your custom view resigns first responder, set the [`displayMode`](nstextinsertionindicator/displaymode-swift.property.md) to [`NSTextInsertionIndicator.DisplayMode.hidden`](nstextinsertionindicator/displaymode-swift.enum/hidden.md) to indicate that key events aren’t sent to your view.

## See Also

- [var automaticModeOptions: NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.property.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/displaymode-swift.property)*