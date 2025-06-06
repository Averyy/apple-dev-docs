# strokeStart

**Framework**: MapKit  
**Kind**: property

The unit distance along the line where the stroke starts.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var strokeStart: CGFloat { get set }
```

#### Discussion

Use this property and [`strokeEnd`](mkpolylinerenderer/strokeend.md) to render a portion of the line. Use [`location(atPointIndex:)`](mkmultipoint/location(atpointindex:).md) to get unit distance locations for point indices along the line.

## See Also

- [var strokeEnd: CGFloat](mkpolylinerenderer/strokeend.md)
  The unit distance along the line where the stroke ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/strokestart)*