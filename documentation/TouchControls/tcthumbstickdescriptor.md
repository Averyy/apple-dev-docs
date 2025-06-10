# TCThumbstickDescriptor

**Framework**: Touch Controls  
**Kind**: class

A descriptor for configuring a thumbstick.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCThumbstickDescriptor
```

## Topics

### Initializers
- [init()](tcthumbstickdescriptor/init.md)
  Creates a new thumbstick descriptor with default values.
### Instance Properties
- [var anchor: TCTransformAnchor](tcthumbstickdescriptor/anchor.md)
  The anchor point that the thumbstick’s offset is relative to.
- [var backgroundVisuals: TCControlVisuals?](tcthumbstickdescriptor/backgroundvisuals.md)
  The visuals for the background of the thumbstick.
- [var colliderType: TCColliderType](tcthumbstickdescriptor/collidertype.md)
  The type of collider to use for the thumbstick.
- [var hideWhenNotPressed: Bool](tcthumbstickdescriptor/hidewhennotpressed.md)
  Whether to hide the thumbstick when it is not being pressed.
- [var highlightTime: simd_float1](tcthumbstickdescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tcthumbstickdescriptor/label.md)
  The label associated with the thumbstick.
- [var layer: simd_int1](tcthumbstickdescriptor/layer.md)
  The layer of the thumbstick, used for z-sorting.
- [var offset: CGPoint](tcthumbstickdescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcthumbstickdescriptor/size.md)
  The size (width, height) of the thumbstick in points.
- [var stickSize: CGSize](tcthumbstickdescriptor/sticksize.md)
  The size (width, height) of the thumbstick stick itself in points.
- [var stickVisuals: TCControlVisuals?](tcthumbstickdescriptor/stickvisuals.md)
  The visuals for the thumbstick itself.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcthumbstickdescriptor)*