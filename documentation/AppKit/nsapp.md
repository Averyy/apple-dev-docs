# NSApp

**Framework**: AppKit  
**Kind**: var

The global variable for the shared app instance.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var NSApp: NSApplication!
```

#### Discussion

The value in this global variable is the same as accessing the [`shared`](nsapplication/shared.md) property of the app.

## See Also

- [class var shared: NSApplication](nsapplication/shared.md)
  Returns the application instance, creating it if it doesn’t exist yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapp)*