# invalidatePath()

**Framework**: MapKit  
**Kind**: method

Updates the path associated with the overlay renderer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func invalidatePath()
```

#### Discussion

Call this method when a change in the path information would require you to recreate the overlay’s path. This method sets the [`path`](mkoverlaypathrenderer/path.md) property to `nil` and tells the overlay renderer to redisplay its contents.

## See Also

- [var path: CGPath!](mkoverlaypathrenderer/path.md)
  The path representing the overlay’s shape.
- [func createPath()](mkoverlaypathrenderer/createpath.md)
  Creates the path for the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/invalidatepath())*