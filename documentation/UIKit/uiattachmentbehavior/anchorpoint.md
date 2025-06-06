# anchorPoint

**Framework**: UIKit  
**Kind**: property

The anchor point for the attachment behavior, if any.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var anchorPoint: CGPoint { get set }
```

#### Discussion

The anchor point is relative to the coordinate system for the behavior’s associated dynamic animator. For attachment types without an anchor point, the value in this property is [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero). For more information about the coordinate system of the reference view, see [`UIDynamicAnimator`](uidynamicanimator.md).

## See Also

- [var attachedBehaviorType: UIAttachmentBehavior.AttachmentType](uiattachmentbehavior/attachedbehaviortype.md)
  The type of the attachment behavior.
- [var damping: CGFloat](uiattachmentbehavior/damping.md)
  The amount of damping to apply to the attachment behavior.
- [var frequency: CGFloat](uiattachmentbehavior/frequency.md)
  The frequency of oscillation for the attachment behavior.
- [var length: CGFloat](uiattachmentbehavior/length.md)
  The distance, in points, between the two attachment points of the attachment behavior.
- [var frictionTorque: CGFloat](uiattachmentbehavior/frictiontorque.md)
  The amount of force needed to overcome rotational forces around an anchor point.
- [var attachmentRange: UIFloatRange](uiattachmentbehavior/attachmentrange.md)
  The range of motion for the attachment behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/anchorpoint)*