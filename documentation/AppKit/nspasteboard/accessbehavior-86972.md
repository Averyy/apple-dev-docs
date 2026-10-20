# accessBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var accessBehavior: NSPasteboard.AccessBehavior { get }
```

```objc
@property (assign, readonly) NSPasteboardAccessBehavior accessBehavior;
```

## See Also

### Determining pasteboard access
- [var accessBehavior: NSPasteboard.AccessBehavior](./accessbehavior-9k4t4.md)
  The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.
- [NSPasteboard.AccessBehavior](./accessbehavior-swift.enum.md)
  A value indicating pasteboard access behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-86972)*