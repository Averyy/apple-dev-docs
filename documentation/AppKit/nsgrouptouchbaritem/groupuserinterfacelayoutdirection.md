# groupUserInterfaceLayoutDirection

**Framework**: AppKit  
**Kind**: property

The user interface direction that controls the layout order of the items.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
var groupUserInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }
```

#### Discussion

The default value is [`NSUserInterfaceLayoutDirection.leftToRight`](nsuserinterfacelayoutdirection/lefttoright.md).

If you want the order of the items in the group to respect the user’s preferred layout, set this property to the value of [`userInterfaceLayoutDirection`](nsapplication/userinterfacelayoutdirection.md) on the [`NSApplication`](nsapplication.md).

## See Also

- [var groupTouchBar: NSTouchBar](nsgrouptouchbaritem/grouptouchbar.md)
  A bar that holds this group’s items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/groupuserinterfacelayoutdirection)*