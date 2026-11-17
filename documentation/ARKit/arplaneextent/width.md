# width

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The estimated width of the plane.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var width: Float { get }
```

```objc
@property (nonatomic, readonly) float width;
```

## Discussion

This corresponds to the length of the plane along the x-axis, prior to applying `rotationOnYAxis`.

## See Also

### Inspecting Plane Size
- [var height: Float](./height.md)
  The estimated height of the plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneextent/width)*