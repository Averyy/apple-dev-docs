# exitFullScreenMode(options:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Instructs the panel to exit full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func exitFullScreenMode(options: [AnyHashable : Any]! = [:])
```

```objc
- (void) exitFullScreenModeWithOptions:(NSDictionary *) options;
```

## Parameters

- `options`: This parameter isn’t used — pass `nil`.

## See Also

### Managing Full Screen Mode
- [func enterFullScreenMode(NSScreen!, withOptions: [AnyHashable : Any]!) -> Bool](./enterfullscreenmode%28_,withoptions%29.md)
  Instructs the panel to enter full screen mode.
- [var isInFullScreenMode: Bool](./isinfullscreenmode.md)
  The property that indicates whether the panel is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/exitfullscreenmode(options:))*