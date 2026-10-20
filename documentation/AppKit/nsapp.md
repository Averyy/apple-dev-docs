# NSApp

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The global variable for the shared app instance.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
var NSApp: NSApplication!
```

```c
extern NSApplication * NSApp;
```

#### Discussion

The value in this global variable is the same as accessing the [`shared`](./nsapplication/shared.md) property of the app.

## See Also

### Getting the shared app object
- [class var shared: NSApplication](./nsapplication/shared.md)
  Returns the application instance, creating it if it doesn’t exist yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapp)*