# enterFullScreenMode(_:withOptions:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Instructs the panel to enter full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func enterFullScreenMode(_ screen: NSScreen!, withOptions options: [AnyHashable : Any]! = [:]) -> Bool
```

```objc
- (BOOL) enterFullScreenMode:(NSScreen *) screen withOptions:(NSDictionary *) options;
```

## Return Value

[`true`](../../Swift/true.md) if the panel was able to enter full screen mode; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the panel isn’t onscreen, the panel goes directly to full screen mode.

The panel chooses the appropriate screen depending on where the panel is or, if entering fullscreen directly, where the panel zooms from.

## Parameters

- `screen`: This parameter isn’t currently used—pass `nil`.
- `options`: This parameter isn’t currently used—pass `nil`.

## See Also

### Managing Full Screen Mode
- [func exitFullScreenMode(options: [AnyHashable : Any]!)](./exitfullscreenmode%28options%29.md)
  Instructs the panel to exit full screen mode.
- [var isInFullScreenMode: Bool](./isinfullscreenmode.md)
  The property that indicates whether the panel is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/enterfullscreenmode(_:withoptions:))*