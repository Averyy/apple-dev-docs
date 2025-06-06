# init(item:offsetFromCenter:attachedToAnchor:)

**Framework**: UIKit  
**Kind**: init

Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(item: any UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint)
```

#### Return Value

The initialized attachment behavior, or `nil` if there was a problem initializing the object.

#### Discussion

The behavior created by this method acts like a solid rod connecting the item to the specified anchor point. The item is free to rotate around the anchor point, but its distance to the anchor point remains fixed. If you specify a nonzero offset value, the item is connected at the specified point instead of the center of the item.

The attachment object returned by this method is of type [`UIAttachmentBehavior.AttachmentType.anchor`](uiattachmentbehavior/attachmenttype/anchor.md).

## Parameters

- `item`: The dynamic item to attach to the specified  .
- `offset`: The offset from the center of   at which to create the attachment. Specifying   creates the attachment at the center of  .
- `point`: The anchor point for the item. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see  .

## See Also

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
- [init(item: any UIDynamicItem, offsetFromCenter: UIOffset, attachedTo: any UIDynamicItem, offsetFromCenter: UIOffset)](uiattachmentbehavior/init(item:offsetfromcenter:attachedto:offsetfromcenter:).md)
  Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/init(item:offsetfromcenter:attachedtoanchor:))*