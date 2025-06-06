# holdingPriority

**Framework**: AppKit  
**Kind**: property

The priority for a split view item to hold its size.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var holdingPriority: NSLayoutConstraint.Priority { get set }
```

#### Discussion

This priority affects the split view item’s width (for a vertical split view) or height (for a horizontal split view).

The view with the lowest priority is the first to gain additional width if the split view grows or shrinks. The default of this property is [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/holdingpriority)*