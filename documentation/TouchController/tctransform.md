# TCTransform

**Framework**: Touch Controller  
**Kind**: protocol

A protocol defining the transform properties for a control.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol TCTransform : NSObjectProtocol
```

## Topics

### Inspecting the transform
- [var layer: simd_int1](tctransform/layer.md)
  The layer of the transform, used for z-ordering.
- [var offset: CGPoint](tctransform/offset.md)
  The offset from the anchor point.
- [var size: CGSize](tctransform/size.md)
  The size of the transform in points.
### Accessing the transform anchor
- [var anchor: TCTransformAnchor](tctransform/anchor.md)
  The anchor point of the transform.
- [enum TCTransformAnchor](tctransformanchor.md)
  Defines the anchor point for a transform.
### Getting the position
- [func position() -> CGPoint](tctransform/position.md)
  The calculated position of the transform.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [TCControl](tccontrol.md)
### Conforming Types
- [TCButton](tcbutton.md)
- [TCDirectionPad](tcdirectionpad.md)
- [TCThrottle](tcthrottle.md)
- [TCThumbstick](tcthumbstick.md)
- [TCTouchpad](tctouchpad.md)

## See Also

- [init(transform: any TCTransform)](tccirclecollider/init(transform:).md)
  Creates a new circle collider with the specified transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctransform)*