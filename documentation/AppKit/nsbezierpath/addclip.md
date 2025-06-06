# addClip()

**Framework**: AppKit  
**Kind**: method

Intersects the area enclosed by the path with the clipping path of the current graphics context and makes the resulting shape the current clipping path.

**Availability**:
- macOS ?+

## Declaration

```swift
func addClip()
```

#### Discussion

This method uses the current winding rule to determine the clipping shape of the receiver. This method does not affect the receiver’s path.

## See Also

- [func setClip()](nsbezierpath/setclip.md)
  Replaces the clipping path of the current graphics context with the area inside the path.
- [class func clip(NSRect)](nsbezierpath/clip(_:).md)
  Intersects the specified rectangle with the clipping path of the current graphics context and makes the resulting shape the current clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/addclip())*