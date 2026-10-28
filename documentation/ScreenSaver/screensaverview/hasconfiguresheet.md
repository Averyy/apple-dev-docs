# hasConfigureSheet

**Framework**: Screen Saver  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the screen saver has an associated configuration sheet.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var hasConfigureSheet: Bool { get }
```

```objc
@property (readonly) BOOL hasConfigureSheet;
```

## Discussion

If you provide a configuration sheet in your bundle, override this method and return [`true`](../../Swift/true.md).

## See Also

### Accessing the configuration sheet
- [var configureSheet: NSWindow?](./configuresheet.md)
  The window that contains the controls to configure the screen saver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/hasconfiguresheet)*