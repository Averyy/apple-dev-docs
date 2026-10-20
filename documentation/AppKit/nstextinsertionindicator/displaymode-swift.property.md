# displayMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value that describes the display mode of an indicator.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var displayMode: NSTextInsertionIndicator.DisplayMode { get set }
```

```objc
@property NSTextInsertionIndicatorDisplayMode displayMode;
```

#### Discussion

Set the [`displayMode`](./displaymode-swift.property.md) to [`NSTextInsertionIndicator.DisplayMode.automatic`](./displaymode-swift.enum/automatic.md) when your custom view becomes the first responder. When your custom view resigns first responder, set the [`displayMode`](./displaymode-swift.property.md) to [`NSTextInsertionIndicator.DisplayMode.hidden`](./displaymode-swift.enum/hidden.md) to indicate that key events aren’t sent to your view.

## See Also

### Setting the display mode
- [var automaticModeOptions: NSTextInsertionIndicator.AutomaticModeOptions](./automaticmodeoptions-swift.property.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.AutomaticModeOptions](./automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.DisplayMode](./displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/displaymode-swift.property)*