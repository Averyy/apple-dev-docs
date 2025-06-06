# isInFullScreenMode

**Framework**: Quick Look UI  
**Kind**: property

The property that indicates whether the panel is in full screen mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var isInFullScreenMode: Bool { get }
```

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/swift/true) if the panel is currently open and in full screen mode; otherwise it’s [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func enterFullScreenMode(NSScreen!, withOptions: [AnyHashable : Any]!) -> Bool](qlpreviewpanel/enterfullscreenmode(_:withoptions:).md)
  Instructs the panel to enter full screen mode.
- [func exitFullScreenMode(options: [AnyHashable : Any]!)](qlpreviewpanel/exitfullscreenmode(options:).md)
  Instructs the panel to exit full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/isinfullscreenmode)*