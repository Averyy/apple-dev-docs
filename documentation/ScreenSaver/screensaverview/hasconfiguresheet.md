# hasConfigureSheet

**Framework**: Screen Saver  
**Kind**: property

A Boolean value that indicates whether the screen saver has an associated configuration sheet.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var hasConfigureSheet: Bool { get }
```

#### Discussion

If you provide a configuration sheet in your bundle, override this method and return [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var configureSheet: NSWindow?](screensaverview/configuresheet.md)
  The window that contains the controls to configure the screen saver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/hasconfiguresheet)*