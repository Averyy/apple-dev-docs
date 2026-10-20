# owningApplication

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The app that owns the window.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var owningApplication: SCRunningApplication? { get }
```

```objc
@property (readonly, nullable) SCRunningApplication * owningApplication;
```

## See Also

### Identifying windows
- [var windowID: CGWindowID](./windowid.md)
  The Core Graphics window identifier.
- [var title: String?](./title.md)
  The string that displays in a window’s title bar.
- [var windowLayer: Int](./windowlayer.md)
  The layer of the window relative to other windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/owningapplication)*