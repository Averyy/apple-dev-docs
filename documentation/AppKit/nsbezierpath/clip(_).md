# clip(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Intersects the specified rectangle with the clipping path of the current graphics context and makes the resulting shape the current clipping path.

**Availability**:
- macOS

## Declaration

```swift
class func clip(_ rect: NSRect)
```

```objc
+ (void) clipRect:(NSRect) rect;
```

## Parameters

- `rect`: The rectangle to intersect with the current clipping path.

## See Also

### Specifying a Clipping Path
- [func addClip()](./addclip%28%29.md)
  Intersects the area enclosed by the path with the clipping path of the current graphics context and makes the resulting shape the current clipping path.
- [func setClip()](./setclip%28%29.md)
  Replaces the clipping path of the current graphics context with the area inside the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/clip(_:))*