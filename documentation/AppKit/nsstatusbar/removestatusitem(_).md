# removeStatusItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified status item from the receiver.

**Availability**:
- macOS

## Declaration

```swift
func removeStatusItem(_ item: NSStatusItem)
```

```objc
- (void) removeStatusItem:(NSStatusItem *) item;
```

## Discussion

Status items to the left of the specified one in the status bar shift to the right to reclaim its space.

## Parameters

- `item`: The `NSStatusItem` object to remove.

## See Also

### Managing Status items
- [func statusItem(withLength: CGFloat) -> NSStatusItem](./statusitem%28withlength%29.md)
  Returns a newly created status item that has been allotted a specified space within the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/removestatusitem(_:))*