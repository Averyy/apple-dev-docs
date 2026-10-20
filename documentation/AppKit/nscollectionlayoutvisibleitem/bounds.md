# bounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The bounds rectangle, which describes the item’s location and size in its own coordinate system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var bounds: NSRect { get }
```

```objc
@property (readonly) NSRect bounds;
```

## See Also

### Configuring position
- [var frame: NSRect](./frame.md)
  The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [var center: NSPoint](./center.md)
  The center point of the item’s frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutvisibleitem/bounds)*