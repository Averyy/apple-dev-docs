# isInFullScreenMode

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

The property that indicates whether the panel is in full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isInFullScreenMode: Bool { get }
```

```objc
@property (readonly, getter=isInFullScreenMode) BOOL inFullScreenMode;
```

#### Discussion

The value is [`true`](../../Swift/true.md) if the panel is currently open and in full screen mode; otherwise it’s [`false`](../../Swift/false.md).

## See Also

### Managing Full Screen Mode
- [func enterFullScreenMode(NSScreen!, withOptions: [AnyHashable : Any]!) -> Bool](./enterfullscreenmode%28_,withoptions%29.md)
  Instructs the panel to enter full screen mode.
- [func exitFullScreenMode(options: [AnyHashable : Any]!)](./exitfullscreenmode%28options%29.md)
  Instructs the panel to exit full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/isinfullscreenmode)*