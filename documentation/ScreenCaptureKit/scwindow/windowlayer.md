# windowLayer

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The layer of the window relative to other windows.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var windowLayer: Int { get }
```

```objc
@property (readonly) NSInteger windowLayer;
```

## See Also

### Identifying windows
- [var windowID: CGWindowID](./windowid.md)
  The Core Graphics window identifier.
- [var title: String?](./title.md)
  The string that displays in a window’s title bar.
- [var owningApplication: SCRunningApplication?](./owningapplication.md)
  The app that owns the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/windowlayer)*