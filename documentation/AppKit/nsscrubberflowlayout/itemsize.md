# itemSize

**Framework**: AppKit  
**Kind**: property

The frame size for each item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var itemSize: NSSize { get set }
```

#### Discussion

You can override the value of this property on a per-item basis, by providing a delegate object to the scrubber that conforms to the [`NSScrubberFlowLayoutDelegate`](nsscrubberflowlayoutdelegate.md) protocol. This delegate object must implement the [`scrubber(_:layout:sizeForItemAt:)`](nsscrubberflowlayoutdelegate/scrubber(_:layout:sizeforitemat:).md) method.

The default value for this property has a width of `50.0` points and a height of `30.0` points.

## See Also

- [var itemSpacing: CGFloat](nsscrubberflowlayout/itemspacing.md)
  The horizontal spacing between items, specified in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayout/itemsize)*