# TCTouchpadDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a touchpad.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCTouchpadDescriptor
```

## Topics

### Creating the descriptor
- [init()](tctouchpaddescriptor/init.md)
  Creates a new touchpad descriptor with default values.
### Inspecting the descriptor
- [var anchor: TCTransformAnchor](tctouchpaddescriptor/anchor.md)
  The anchor point that the touchpad’s offset is relative to.
- [var colliderType: TCColliderType](tctouchpaddescriptor/collidertype.md)
  The type of collider to use for the touchpad.
- [var highlightTime: simd_float1](tctouchpaddescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tctouchpaddescriptor/label.md)
  The label associated with the touchpad.
- [var layer: simd_int1](tctouchpaddescriptor/layer.md)
  The layer of the touchpad, used for z-sorting.
- [var offset: CGPoint](tctouchpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsDeltas: Bool](tctouchpaddescriptor/reportsdeltas.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.
- [var visuals: TCControlVisuals?](tctouchpaddescriptor/visuals.md)
  The visuals for the touchpad.

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

## See Also

- [class TCButtonDescriptor](tcbuttondescriptor.md)
  A descriptor for configuring a button.
- [class TCDirectionPadDescriptor](tcdirectionpaddescriptor.md)
  A descriptor for configuring a directional pad.
- [class TCThumbstickDescriptor](tcthumbstickdescriptor.md)
  A descriptor for configuring a thumbstick.
- [class TCThrottleDescriptor](tcthrottledescriptor.md)
  A descriptor for configuring a throttle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor)*