# title

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The string that displays in a window’s title bar.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (readonly, nullable) NSString * title;
```

## See Also

### Identifying windows
- [var windowID: CGWindowID](./windowid.md)
  The Core Graphics window identifier.
- [var owningApplication: SCRunningApplication?](./owningapplication.md)
  The app that owns the window.
- [var windowLayer: Int](./windowlayer.md)
  The layer of the window relative to other windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow/title)*