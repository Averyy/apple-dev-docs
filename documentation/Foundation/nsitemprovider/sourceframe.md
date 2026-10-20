# sourceFrame

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The rectangle that the item occupies in the host app’s source window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var sourceFrame: NSRect { get }
```

```objc
@property (readonly) NSRect sourceFrame;
```

#### Discussion

This property contains the rectangle, in screen coordinates, that encloses the item. This rectangle includes areas that might be clipped and not currently visible onscreen.

## See Also

### Getting the provider’s frame
- [var containerFrame: NSRect](./containerframe.md)
  The rectangle of the item’s visible content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/sourceframe)*