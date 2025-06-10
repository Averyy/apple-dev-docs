# TCButtonDescriptor

**Framework**: Touch Controls  
**Kind**: class

A descriptor for configuring a button.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCButtonDescriptor
```

## Topics

### Initializers
- [init()](tcbuttondescriptor/init.md)
  Creates a new button descriptor with default values.
### Instance Properties
- [var anchor: TCTransformAnchor](tcbuttondescriptor/anchor.md)
  The anchor point that the button’s offset is relative to.
- [var colliderType: TCColliderType](tcbuttondescriptor/collidertype.md)
  The type of collider to use for the button.
- [var highlightTime: simd_float1](tcbuttondescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isToggle: Bool](tcbuttondescriptor/istoggle.md)
  Whether the button is a toggle button.
- [var label: TCControlLabel](tcbuttondescriptor/label.md)
  The label you associate with the button.
- [var layer: simd_int1](tcbuttondescriptor/layer.md)
  The layer of the button, used for z-sorting.
- [var offset: CGPoint](tcbuttondescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcbuttondescriptor/size.md)
  The size (width, height) of the button in points.
- [var toggleVisuals: TCControlVisuals?](tcbuttondescriptor/togglevisuals.md)
  The visuals for the button when it is toggled on.
- [var visuals: TCControlVisuals?](tcbuttondescriptor/visuals.md)
  The visuals for the button in its normal state.

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

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcbuttondescriptor)*