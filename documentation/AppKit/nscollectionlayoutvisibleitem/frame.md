# frame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The frame rectangle, which describes the item’s location and size in its section’s coordinate system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var frame: NSRect { get }
```

```objc
@property (readonly) NSRect frame;
```

## See Also

### Configuring position
- [var bounds: NSRect](./bounds.md)
  The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [var center: NSPoint](./center.md)
  The center point of the item’s frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutvisibleitem/frame)*