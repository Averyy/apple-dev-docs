# height

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The estimated height of the plane.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var height: Float { get }
```

```objc
@property (nonatomic, readonly) float height;
```

## Discussion

This corresponds to the length of the plane along the z-axis, prior to applying `rotationOnYAxis`.

## See Also

### Inspecting Plane Size
- [var width: Float](./width.md)
  The estimated width of the plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneextent/height)*