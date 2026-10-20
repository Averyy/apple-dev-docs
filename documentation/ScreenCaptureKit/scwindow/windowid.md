# windowID

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The Core Graphics window identifier.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var windowID: CGWindowID { get }
```

```objc
@property (readonly) CGWindowID windowID;
```

## See Also

### Identifying windows
- [var title: String?](./title.md)
  The string that displays in a window’s title bar.
- [var owningApplication: SCRunningApplication?](./owningapplication.md)
  The app that owns the window.
- [var windowLayer: Int](./windowlayer.md)
  The layer of the window relative to other windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/windowid)*