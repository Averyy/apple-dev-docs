# limitAttachment(with:offsetFromCenter:attachedTo:offsetFromCenter:)

**Framework**: UIKit  
**Kind**: method

Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func limitAttachment(with item1: any UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedTo item2: any UIDynamicItem, offsetFromCenter offset2: UIOffset) -> Self
```

#### Return Value

A new attachment object or `nil` if the object could not be created.

#### Discussion

The behavior created by this method is like connecting two items with a rope. The only constraint between the items is the maximum distance between them, which corresponds to the moment when the rope is taut. At other times, the objects move freely relative to one another.

The initial maximum distance between the items is set using the current position of the items. You can change the maximum distance by modifying the [`length`](uiattachmentbehavior/length.md) property.

## Parameters

- `item1`: The first of two dynamic items connected by the attachment behavior.
- `offset1`: The offset from the center of   that corresponds to the attachment point. Use an offset value to create rotational torque on the item. To pull the item from its center, specify  .
- `item2`: The second of two dynamic items connected by the attachment behavior.
- `offset2`: The offset from the center of   that corresponds to the attachment point. Use an offset value to create rotational torque on the item. To pull the item from its center, specify  .

## See Also

- [class func slidingAttachment(with: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](uiattachmentbehavior/slidingattachment(with:attachmentanchor:axisoftranslation:).md)
  Creates and returns an attachment behavior where one item slides along the specified axis.
- [class func slidingAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](uiattachmentbehavior/slidingattachment(with:attachedto:attachmentanchor:axisoftranslation:).md)
  Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [class func fixedAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint) -> Self](uiattachmentbehavior/fixedattachment(with:attachedto:attachmentanchor:).md)
  Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/limitattachment(with:offsetfromcenter:attachedto:offsetfromcenter:))*