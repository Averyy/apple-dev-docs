# setMenu(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the menu for the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setMenu(_ menu: NSMenu?, forSegment segment: Int)
```

#### Discussion

Adding a menu to a segment allows the segment to be used as a pop-up button. If the segment has a menu only, then the menu displays when the user clicks the segment. If the segment has both a menu and an action, then the action triggers when the user clicks the segment and the menu displays when the user clicks and holds the segment.

## Parameters

- `menu`: The menu you want to add to the segment or   to clear the current menu.
- `segment`: The index of the segment whose menu you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func menu(forSegment: Int) -> NSMenu?](nssegmentedcontrol/menu(forsegment:).md)
  Returns the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](nssegmentedcontrol/setshowsmenuindicator(_:forsegment:).md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](nssegmentedcontrol/showsmenuindicator(forsegment:).md)
- [var isSpringLoaded: Bool](nssegmentedcontrol/isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setmenu(_:forsegment:))*