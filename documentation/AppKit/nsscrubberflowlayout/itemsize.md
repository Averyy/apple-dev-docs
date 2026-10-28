# itemSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The frame size for each item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var itemSize: NSSize { get set }
```

```objc
@property NSSize itemSize;
```

## Discussion

You can override the value of this property on a per-item basis, by providing a delegate object to the scrubber that conforms to the [`NSScrubberFlowLayoutDelegate`](../nsscrubberflowlayoutdelegate.md) protocol. This delegate object must implement the [`scrubber(_:layout:sizeForItemAt:)`](../nsscrubberflowlayoutdelegate/scrubber%28_,layout,sizeforitemat%29.md) method.

The default value for this property has a width of `50.0` points and a height of `30.0` points.

## See Also

### Configuring the layout
- [var itemSpacing: CGFloat](./itemspacing.md)
  The horizontal spacing between items, specified in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayout/itemsize)*