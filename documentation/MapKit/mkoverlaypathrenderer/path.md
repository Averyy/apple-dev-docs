# path

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The path representing the overlay’s shape.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var path: CGPath! { get set }
```

```objc
@property (null_resettable) CGPathRef path;
```

## Discussion

Getting the value of this property causes the method to create the path (using the [`createPath()`](./createpath%28%29.md) method) if it doesn’t already exist. You can assign a path object to this property explicitly. When assigning a new path object to this property, the overlay renderer stores a strong reference to the path you provide.

## See Also

### Creating and managing the path
- [func createPath()](./createpath%28%29.md)
  Creates the path for the overlay.
- [func invalidatePath()](./invalidatepath%28%29.md)
  Updates the path associated with the overlay renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/path)*