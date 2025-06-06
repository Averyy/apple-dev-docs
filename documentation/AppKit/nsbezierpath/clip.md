# clip(_:)

**Framework**: AppKit  
**Kind**: method

Intersects the specified rectangle with the clipping path of the current graphics context and makes the resulting shape the current clipping path.

**Availability**:
- macOS ?+

## Declaration

```swift
class func clip(_ rect: NSRect)
```

## Parameters

- `rect`: The rectangle to intersect with the current clipping path.

## See Also

- [func addClip()](nsbezierpath/addclip.md)
  Intersects the area enclosed by the path with the clipping path of the current graphics context and makes the resulting shape the current clipping path.
- [func setClip()](nsbezierpath/setclip.md)
  Replaces the clipping path of the current graphics context with the area inside the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/clip(_:))*