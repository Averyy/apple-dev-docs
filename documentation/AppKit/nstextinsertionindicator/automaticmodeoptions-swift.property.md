# automaticModeOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Options that affect the automatic display mode.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var automaticModeOptions: NSTextInsertionIndicator.AutomaticModeOptions { get set }
```

```objc
@property NSTextInsertionIndicatorAutomaticModeOptions automaticModeOptions;
```

## Mentions

- [Adopting the system text cursor in custom text views](../adopting-the-system-text-cursor-in-custom-text-views.md)

#### Discussion

Defaults to [`showEffectsView`](./automaticmodeoptions-swift.struct/showeffectsview.md).

## See Also

### Setting the display mode
- [var displayMode: NSTextInsertionIndicator.DisplayMode](./displaymode-swift.property.md)
  A value that describes the display mode of an indicator.
- [NSTextInsertionIndicator.AutomaticModeOptions](./automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.
- [NSTextInsertionIndicator.DisplayMode](./displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/automaticmodeoptions-swift.property)*