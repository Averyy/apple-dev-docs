# sourceFrame

**Framework**: Foundation  
**Kind**: property

The rectangle that the item occupies in the host app’s source window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var sourceFrame: NSRect { get }
```

#### Discussion

This property contains the rectangle, in screen coordinates, that encloses the item. This rectangle includes areas that might be clipped and not currently visible onscreen.

## See Also

- [var containerFrame: NSRect](nsitemprovider/containerframe.md)
  The rectangle of the item’s visible content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/sourceframe)*