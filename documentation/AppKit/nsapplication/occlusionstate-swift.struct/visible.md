# visible

**Framework**: AppKit  
**Kind**: property

If set, at least part of any window owned by this app is visible.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var visible: NSApplication.OcclusionState { get }
```

#### Discussion

If not set, all parts of all windows owned by this app are completely occluded. The menu bar does not count as a window owned by this app, so if only the menu bar is showing then the app is considered not visible. Status items, however, have windows owned by your app. If the status item is present in the menu bar, your app will be considered visible as long as the menu bar is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/occlusionstate-swift.struct/visible)*