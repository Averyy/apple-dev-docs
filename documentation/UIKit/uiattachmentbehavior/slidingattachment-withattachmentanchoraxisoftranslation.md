# slidingAttachment(with:attachmentAnchor:axisOfTranslation:)

**Framework**: UIKit  
**Kind**: method

Creates and returns an attachment behavior where one item slides along the specified axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func slidingAttachment(with item: any UIDynamicItem, attachmentAnchor point: CGPoint, axisOfTranslation axis: CGVector) -> Self
```

#### Return Value

A new attachment object or `nil` if the object could not be created.

#### Discussion

The behavior created by this method acts like a solid rod between `item` and the anchor point whose initial position you specify using the `point` parameter. As forces are applied to the item, the item’s anchor point slides along the specified `axis`, causing the item to move with it. The item does not rotate relative to the axis of translation or anchor point.

The axis of translation is infinitely long initially, but you can change the length by assigning a new value to the [`attachmentRange`](uiattachmentbehavior/attachmentrange.md) property. When specifying a new attachment range, remember that the value in point represents the value `0` on the axis. Any new range you specify must include `0`.

You can use this behavior to create an effect of an item sliding in a specific direction in response to other forces. For example, using the vector (0.0, 1.0) would cause the item to slide only vertically.

## Parameters

- `item`: The dynamic item connected by the attachment behavior.
- `point`: The initial anchor point for the item. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see  .
- `axis`: The axis of translation, along which the item’s anchor point slides. The magnitude of the vector is ignored. Use the   property to define the distance that the anchor point can travel along the vector.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/slidingattachment(with:attachmentanchor:axisoftranslation:))*