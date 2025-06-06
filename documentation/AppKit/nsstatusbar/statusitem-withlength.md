# statusItem(withLength:)

**Framework**: AppKit  
**Kind**: method

Returns a newly created status item that has been allotted a specified space within the status bar.

**Availability**:
- macOS ?+

## Declaration

```swift
func statusItem(withLength length: CGFloat) -> NSStatusItem
```

#### Return Value

An [`NSStatusItem`](nsstatusitem.md) object.

#### Discussion

The receiver does not retain a reference to the status item, so you need to retain it. Otherwise, the object is removed from the status bar when it is deallocated.

## Parameters

- `length`: A constant that specifies whether the status item is of fixed width, or variable width. The valid constants are described in  .

## See Also

- [func removeStatusItem(NSStatusItem)](nsstatusbar/removestatusitem(_:).md)
  Removes the specified status item from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/statusitem(withlength:))*