# containerFrame

**Framework**: Foundation  
**Kind**: property

The rectangle of the item’s visible content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var containerFrame: NSRect { get }
```

#### Discussion

The rectangle in this property corresponds to the onscreen frame rectangle of the item. This rectangle may or may not intersect the [`sourceFrame`](nsitemprovider/sourceframe.md) rectangle of the item. An intersection of the rectangles means that at least part of the item is visible onscreen.

The rectangle in this property may be a clipped version of the source frame or it might be [`NSZeroRect`](nszerorect.md) if the item is offscreen or the system can’t determine the clipping rectangle. The system treats a value of [`NSZeroRect`](nszerorect.md) as meaning the item is fully visible.

## See Also

- [var sourceFrame: NSRect](nsitemprovider/sourceframe.md)
  The rectangle that the item occupies in the host app’s source window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/containerframe)*