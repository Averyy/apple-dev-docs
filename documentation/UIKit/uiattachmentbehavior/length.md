# length

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance, in points, between the two attachment points of the attachment behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var length: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat length;
```

## Discussion

Use this property to adjust the attachment length, if you want to, *after* creating an attachment. The system sets initial length automatically based on how you initialize the attachment.

## See Also

### Configuring an attachment behavior
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point for the attachment behavior, if any.
- [var attachedBehaviorType: UIAttachmentBehavior.AttachmentType](./attachedbehaviortype.md)
  The type of the attachment behavior.
- [var damping: CGFloat](./damping.md)
  The amount of damping to apply to the attachment behavior.
- [var frequency: CGFloat](./frequency.md)
  The frequency of oscillation for the attachment behavior.
- [var frictionTorque: CGFloat](./frictiontorque.md)
  The amount of force needed to overcome rotational forces around an anchor point.
- [var attachmentRange: UIFloatRange](./attachmentrange.md)
  The range of motion for the attachment behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/length)*