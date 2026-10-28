# strokeStart

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) CGFloat strokeStart;
```

## Discussion

Use this property and [`strokeEnd`](./strokeend.md) to render a portion of the line. Use [`location(atPointIndex:)`](../mkmultipoint/location%28atpointindex%29.md) to get unit distance locations for point indices along the line.

## See Also

### Accessing the stroke
- [var strokeEnd: CGFloat](./strokeend.md)
  The unit distance along the line where the stroke ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/strokestart)*