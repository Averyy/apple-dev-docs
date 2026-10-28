# isActive

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the window is currently streaming.

**Availability**:
- Mac Catalyst 18.2+
- macOS 13.1+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (readonly, getter=isActive) BOOL active;
```

## Discussion

When this value is `true`, the window is currently streaming, even if offscreen.

## See Also

### Determining visibility
- [var isOnScreen: Bool](./isonscreen.md)
  A Boolean value that indicates whether the window is on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/isactive)*