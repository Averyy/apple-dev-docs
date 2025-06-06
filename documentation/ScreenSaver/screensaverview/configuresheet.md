# configureSheet

**Framework**: Screen Saver  
**Kind**: property

The window that contains the controls to configure the screen saver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var configureSheet: NSWindow? { get }
```

#### Discussion

The system runs this window as a sheet, so include buttons that allow the user to end the modal session in which the sheet runs. When the user dismisses the sheet, the controller in charge of the sheet must end the document modal session by calling the [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) method [`endSheet(_:)`](https://developer.apple.com/documentation/AppKit/NSApplication/endSheet(_:)) with the sheet’s window as the argument.

## See Also

- [var hasConfigureSheet: Bool](screensaverview/hasconfiguresheet.md)
  A Boolean value that indicates whether the screen saver has an associated configuration sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/configuresheet)*