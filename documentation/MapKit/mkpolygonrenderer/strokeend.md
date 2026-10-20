# strokeEnd

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The unit distance along the polygon where the stroke ends.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var strokeEnd: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat strokeEnd;
```

#### Discussion

Use this property and [`strokeStart`](./strokestart.md) to render a portion of the polygon. Use [`location(atPointIndex:)`](../mkmultipoint/location%28atpointindex%29.md) to get unit distance locations for point indices along the polygon.

## See Also

### Accessing the stroke
- [var strokeStart: CGFloat](./strokestart.md)
  The unit distance along the polygon where the stroke starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/strokeend)*