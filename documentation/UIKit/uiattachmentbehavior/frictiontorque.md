# frictionTorque

**Framework**: UIKit  
**Kind**: property

The amount of force needed to overcome rotational forces around an anchor point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var frictionTorque: CGFloat { get set }
```

#### Discussion

For attachments where each item rotates around an anchor point, use this property to specify the resistance to that rotation. The default value of this property is `0.0`, which causes items to rotate freely with even very small impulses. Higher torque values increase the amount of force needed to cause rotation.

This property has no formal units, so you need to experiment with values to get the behavior that you want.

## See Also

- [var anchorPoint: CGPoint](uiattachmentbehavior/anchorpoint.md)
  The anchor point for the attachment behavior, if any.
- [var attachedBehaviorType: UIAttachmentBehavior.AttachmentType](uiattachmentbehavior/attachedbehaviortype.md)
  The type of the attachment behavior.
- [var damping: CGFloat](uiattachmentbehavior/damping.md)
  The amount of damping to apply to the attachment behavior.
- [var frequency: CGFloat](uiattachmentbehavior/frequency.md)
  The frequency of oscillation for the attachment behavior.
- [var length: CGFloat](uiattachmentbehavior/length.md)
  The distance, in points, between the two attachment points of the attachment behavior.
- [var attachmentRange: UIFloatRange](uiattachmentbehavior/attachmentrange.md)
  The range of motion for the attachment behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/frictiontorque)*