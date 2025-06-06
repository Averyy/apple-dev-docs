# removeStatusItem(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified status item from the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeStatusItem(_ item: NSStatusItem)
```

#### Discussion

Status items to the left of the specified one in the status bar shift to the right to reclaim its space.

## Parameters

- `item`: The   object to remove.

## See Also

- [func statusItem(withLength: CGFloat) -> NSStatusItem](nsstatusbar/statusitem(withlength:).md)
  Returns a newly created status item that has been allotted a specified space within the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/removestatusitem(_:))*