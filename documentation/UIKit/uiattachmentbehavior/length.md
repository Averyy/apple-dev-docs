# length

**Framework**: UIKit  
**Kind**: property

The distance, in points, between the two attachment points of the attachment behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var length: CGFloat { get set }
```

#### Discussion

Use this property to adjust the attachment length, if you want to,  creating an attachment. The system sets initial length automatically based on how you initialize the attachment.

## See Also

- [var anchorPoint: CGPoint](uiattachmentbehavior/anchorpoint.md)
  The anchor point for the attachment behavior, if any.
- [var attachedBehaviorType: UIAttachmentBehavior.AttachmentType](uiattachmentbehavior/attachedbehaviortype.md)
  The type of the attachment behavior.
- [var damping: CGFloat](uiattachmentbehavior/damping.md)
  The amount of damping to apply to the attachment behavior.
- [var frequency: CGFloat](uiattachmentbehavior/frequency.md)
  The frequency of oscillation for the attachment behavior.
- [var frictionTorque: CGFloat](uiattachmentbehavior/frictiontorque.md)
  The amount of force needed to overcome rotational forces around an anchor point.
- [var attachmentRange: UIFloatRange](uiattachmentbehavior/attachmentrange.md)
  The range of motion for the attachment behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/length)*