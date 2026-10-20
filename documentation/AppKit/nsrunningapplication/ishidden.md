# isHidden

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the application is currently hidden.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isHidden: Bool { get }
```

```objc
@property (readonly, getter=isHidden) BOOL hidden;
```

#### Discussion

This property is observable using key-value observing.

## See Also

### Hiding and unhiding applications
- [func hide() -> Bool](./hide%28%29.md)
  Attempts to hide or the application.
- [func unhide() -> Bool](./unhide%28%29.md)
  Attempts to unhide or the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/ishidden)*