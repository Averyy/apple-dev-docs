# enterFullScreenMode(_:withOptions:)

**Framework**: Quick Look UI  
**Kind**: method

Instructs the panel to enter full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func enterFullScreenMode(_ screen: NSScreen!, withOptions options: [AnyHashable : Any]! = [:]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the panel was able to enter full screen mode; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the panel isn’t onscreen, the panel goes directly to full screen mode.

The panel chooses the appropriate screen depending on where the panel is or, if entering fullscreen directly, where the panel zooms from.

## Parameters

- `screen`: This parameter isn’t currently used—pass  .
- `options`: This parameter isn’t currently used—pass  .

## See Also

- [func exitFullScreenMode(options: [AnyHashable : Any]!)](qlpreviewpanel/exitfullscreenmode(options:).md)
  Instructs the panel to exit full screen mode.
- [var isInFullScreenMode: Bool](qlpreviewpanel/isinfullscreenmode.md)
  The property that indicates whether the panel is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/enterfullscreenmode(_:withoptions:))*