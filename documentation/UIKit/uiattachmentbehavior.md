# UIAttachmentBehavior

**Framework**: UIKit  
**Kind**: class

A relationship between two dynamic items, or between a dynamic item and an anchor point.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAttachmentBehavior
```

#### Overview

When two items are attached to each other, forces imparted on one item affect the movement of the other in a prescribed way. When an item is attached to an anchor point, the movement of that item is affected by its attachment to the specified anchor point. Some attachment behaviors support both two items and an anchor point.

You specify type of attachment behavior you want at creation time. This class offers many creation and initialization methods, each of which creates a different type of attachment behavior, which cannot be changed later. However, you may change specific attributes of the attachment behavior using the properties of this class. For example, you can change the distance between two attached items or change the damping forces applied to the items.

##### Applying an Attachment Behavior to Dynamic Items

To apply an attachment behavior to your dynamic items, do the following:

1. Create the attachment behavior using one of the creation or initialization methods. The method you choose defines the relationship between the items and the anchor point (if any).
2. Enable the attachment behavior by adding it to your [`UIDynamicAnimator`](uidynamicanimator.md) object using the [`addBehavior(_:)`](uidynamicanimator/addbehavior(_:).md) method. Do not add the same attachment behavior to multiple animator objects.

The attachment behavior derives its coordinate system from the reference view of its associated dynamic animator object. For more information about the dynamic animator and the reference coordinate system, see [`UIDynamicAnimator`](uidynamicanimator.md).

## Topics

### Creating and initializing attachment behavior objects
- [class func slidingAttachment(with: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](uiattachmentbehavior/slidingattachment(with:attachmentanchor:axisoftranslation:).md)
  Creates and returns an attachment behavior where one item slides along the specified axis.
- [class func slidingAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](uiattachmentbehavior/slidingattachment(with:attachedto:attachmentanchor:axisoftranslation:).md)
  Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [class func fixedAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint) -> Self](uiattachmentbehavior/fixedattachment(with:attachedto:attachmentanchor:).md)
  Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [class func limitAttachment(with: any UIDynamicItem, offsetFromCenter: UIOffset, attachedTo: any UIDynamicItem, offsetFromCenter: UIOffset) -> Self](uiattachmentbehavior/limitattachment(with:offsetfromcenter:attachedto:offsetfromcenter:).md)
  Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [class func pinAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint) -> Self](uiattachmentbehavior/pinattachment(with:attachedto:attachmentanchor:).md)
  Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [convenience init(item: any UIDynamicItem, attachedToAnchor: CGPoint)](uiattachmentbehavior/init(item:attachedtoanchor:).md)
  Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [convenience init(item: any UIDynamicItem, attachedTo: any UIDynamicItem)](uiattachmentbehavior/init(item:attachedto:).md)
  Initializes a behavior where the centers of two dynamic items are attached to each other.
- [init(item: any UIDynamicItem, offsetFromCenter: UIOffset, attachedToAnchor: CGPoint)](uiattachmentbehavior/init(item:offsetfromcenter:attachedtoanchor:).md)
  Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [init(item: any UIDynamicItem, offsetFromCenter: UIOffset, attachedTo: any UIDynamicItem, offsetFromCenter: UIOffset)](uiattachmentbehavior/init(item:offsetfromcenter:attachedto:offsetfromcenter:).md)
  Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.
### Getting the attached items
- [var items: [any UIDynamicItem]](uiattachmentbehavior/items.md)
  The dynamic items connected by the attachment behavior.
### Configuring an attachment behavior
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
- [var frictionTorque: CGFloat](uiattachmentbehavior/frictiontorque.md)
  The amount of force needed to overcome rotational forces around an anchor point.
- [var attachmentRange: UIFloatRange](uiattachmentbehavior/attachmentrange.md)
  The range of motion for the attachment behavior.
### Constants
- [UIAttachmentBehavior.AttachmentType](uiattachmentbehavior/attachmenttype.md)
  Constants indicating the type of the attachment behavior object.
- [struct UIFloatRange](uifloatrange.md)
  The range of motion for attached objects.
- [Float range constants](float-range-constants.md)
  Constants for specifying standard ranges.
- [struct UIOffset](uioffset.md)
  A structure that specifies an amount to offset a position.

## Relationships

### Inherits From
- [UIDynamicBehavior](uidynamicbehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIDynamicBehavior](uidynamicbehavior.md)
  An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [class UICollisionBehavior](uicollisionbehavior.md)
  An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [class UIFieldBehavior](uifieldbehavior.md)
  An object that applies field-based physics to dynamic items.
- [class UIGravityBehavior](uigravitybehavior.md)
  An object that applies a gravity-like force to all of its associated dynamic items.
- [class UIPushBehavior](uipushbehavior.md)
  A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [class UISnapBehavior](uisnapbehavior.md)
  A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior)*