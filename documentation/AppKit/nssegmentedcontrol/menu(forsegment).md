# menu(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu for the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func menu(forSegment segment: Int) -> NSMenu?
```

```objc
- (NSMenu *) menuForSegment:(NSInteger) segment;
```

## Return Value

The menu associated with the segment; otherwise, `nil`.

## Parameters

- `segment`: The index of the segment whose menu you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring a segment menu
- [func setMenu(NSMenu?, forSegment: Int)](./setmenu%28_,forsegment%29.md)
  Sets the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](./setshowsmenuindicator%28_,forsegment%29.md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](./showsmenuindicator%28forsegment%29.md)
- [var isSpringLoaded: Bool](./isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/menu(forsegment:))*