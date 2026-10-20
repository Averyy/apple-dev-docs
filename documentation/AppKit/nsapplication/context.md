# context

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The graphics context associated with the app.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

> **Deprecated**: This method always returns nil. If you need access to the current drawing context, use [NSGraphicsContext currentContext] inside of a draw operation.

## Declaration

```swift
var context: NSGraphicsContext? { get }
```

```objc
@property (strong, readonly, nullable) NSGraphicsContext * context;
```

#### Discussion

This property contains the graphics context most recently used by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/context)*