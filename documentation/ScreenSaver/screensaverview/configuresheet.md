# configureSheet

**Framework**: Screen Saver  
**Kind**: property  
**Role**: Instance Property

The window that contains the controls to configure the screen saver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var configureSheet: NSWindow? { get }
```

```objc
@property (strong, readonly) NSWindow * configureSheet;
```

#### Discussion

The system runs this window as a sheet, so include buttons that allow the user to end the modal session in which the sheet runs. When the user dismisses the sheet, the controller in charge of the sheet must end the document modal session by calling the [`NSApplication`](../../AppKit/nsapplication.md) method [`endSheet(_:)`](../../AppKit/nsapplication/endsheet%28_%29.md) with the sheet’s window as the argument.

## See Also

### Accessing the configuration sheet
- [var hasConfigureSheet: Bool](./hasconfiguresheet.md)
  A Boolean value that indicates whether the screen saver has an associated configuration sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/configuresheet)*