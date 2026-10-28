# strokeEnd

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The unit distance along the circle where the stroke ends.

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

## Discussion

Use this property and [`strokeStart`](./strokestart.md) to render a portion of the line. As a unit distance, [`strokeEnd`](./strokeend.md) must be a value between 0 and 1. A unit distance of 0 represents the top of the circle and the stroke draws in a clockwise direction.

## See Also

### Accessing the stroke
- [var strokeStart: CGFloat](./strokestart.md)
  The unit distance along the circle where the stroke starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/strokeend)*