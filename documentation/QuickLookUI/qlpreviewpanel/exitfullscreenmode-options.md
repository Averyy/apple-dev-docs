# exitFullScreenMode(options:)

**Framework**: Quick Look UI  
**Kind**: method

Instructs the panel to exit full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func exitFullScreenMode(options: [AnyHashable : Any]! = [:])
```

## Parameters

- `options`: This parameter isn’t used — pass  .

## See Also

- [func enterFullScreenMode(NSScreen!, withOptions: [AnyHashable : Any]!) -> Bool](qlpreviewpanel/enterfullscreenmode(_:withoptions:).md)
  Instructs the panel to enter full screen mode.
- [var isInFullScreenMode: Bool](qlpreviewpanel/isinfullscreenmode.md)
  The property that indicates whether the panel is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/exitfullscreenmode(options:))*