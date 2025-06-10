# TCTransform

**Framework**: Touch Controls  
**Kind**: protocol

A protocol defining the transform properties for a control.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
protocol TCTransform : NSObjectProtocol
```

## Topics

### Instance Properties
- [var anchor: TCTransformAnchor](tctransform/anchor.md)
  The anchor point of the transform.
- [var layer: simd_int1](tctransform/layer.md)
  The layer of the transform, used for z-ordering.
- [var offset: CGPoint](tctransform/offset.md)
  The offset from the anchor point.
- [var size: CGSize](tctransform/size.md)
  The size of the transform in points.
### Instance Methods
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tctransform)*