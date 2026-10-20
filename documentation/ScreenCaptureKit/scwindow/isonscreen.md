# isOnScreen

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is on screen.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var isOnScreen: Bool { get }
```

```objc
@property (readonly, getter=isOnScreen) BOOL onScreen;
```

#### Discussion

This value represents the macOS window server’s onscreen status of the window.

## See Also

### Determining visibility
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates if the window is currently streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/isonscreen)*