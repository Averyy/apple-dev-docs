# setMenu(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the menu for the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func setMenu(_ menu: NSMenu?, forSegment segment: Int)
```

```objc
- (void) setMenu:(NSMenu *) menu forSegment:(NSInteger) segment;
```

## Discussion

Adding a menu to a segment allows the segment to be used as a pop-up button. If the segment has a menu only, then the menu displays when the user clicks the segment. If the segment has both a menu and an action, then the action triggers when the user clicks the segment and the menu displays when the user clicks and holds the segment.

## Parameters

- `menu`: The menu you want to add to the segment or `nil` to clear the current menu.
- `segment`: The index of the segment whose menu you want to set. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring a segment menu
- [func menu(forSegment: Int) -> NSMenu?](./menu%28forsegment%29.md)
  Returns the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](./setshowsmenuindicator%28_,forsegment%29.md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](./showsmenuindicator%28forsegment%29.md)
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setmenu(_:forsegment:))*