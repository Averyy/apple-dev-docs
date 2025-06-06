# menu(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the menu for the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func menu(forSegment segment: Int) -> NSMenu?
```

#### Return Value

The menu associated with the segment; otherwise, `nil`.

## Parameters

- `segment`: The index of the segment whose menu you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setMenu(NSMenu?, forSegment: Int)](nssegmentedcontrol/setmenu(_:forsegment:).md)
  Sets the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](nssegmentedcontrol/setshowsmenuindicator(_:forsegment:).md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](nssegmentedcontrol/showsmenuindicator(forsegment:).md)
- [var isSpringLoaded: Bool](nssegmentedcontrol/isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/menu(forsegment:))*