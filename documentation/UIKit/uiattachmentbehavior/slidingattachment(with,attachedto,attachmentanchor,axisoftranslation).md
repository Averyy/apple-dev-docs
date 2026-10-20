# slidingAttachment(with:attachedTo:attachmentAnchor:axisOfTranslation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func slidingAttachment(with item1: any UIDynamicItem, attachedTo item2: any UIDynamicItem, attachmentAnchor point: CGPoint, axisOfTranslation axis: CGVector) -> Self
```

```objc
+ (instancetype) slidingAttachmentWithItem:(id<UIDynamicItem>) item1 attachedToItem:(id<UIDynamicItem>) item2 attachmentAnchor:(CGPoint) point axisOfTranslation:(CGVector) axis;
```

#### Return Value

A new attachment object or `nil` if the object could not be created.

#### Discussion

For this behavior, each item acts like it is at the end of a solid rod attached to its anchor point. Both items start with the same anchor point, but as animations progress, each item’s anchor point is allowed to slide along the specified axis of translation independently. So if one item moves, it pushes the translation axis and the other item with it. The items do not rotate relative to the axis of translation or to each other, but the proximity of the items to one another varies depending on the movement of each item’s anchor point along the translation axis.

The axis of translation is infinitely long initially, but you can change the length by assigning a new value to the [`attachmentRange`](./attachmentrange.md) property. When specifying a new attachment range, remember that the value in point represents the value `0` on the axis. Any new range you specify must include `0`.

## Parameters

- `item1`: The first of two dynamic items connected by the attachment behavior.
- `item2`: The second of two dynamic items connected by the attachment behavior.
- `point`: The initial anchor point for both items. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see [`UIDynamicAnimator`](../uidynamicanimator.md).
- `axis`: The axis of translation, along which the anchor points of the items slide.

## See Also

### Creating and initializing attachment behavior objects
- [class func slidingAttachment(with: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](./slidingattachment%28with,attachmentanchor,axisoftranslation%29.md)
  Creates and returns an attachment behavior where one item slides along the specified axis.
- [class func fixedAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint) -> Self](./fixedattachment%28with,attachedto,attachmentanchor%29.md)
  Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [class func limitAttachment(with: any UIDynamicItem, offsetFromCenter: UIOffset, attachedTo: any UIDynamicItem, offsetFromCenter: UIOffset) -> Self](./limitattachment%28with,offsetfromcenter,attachedto,offsetfromcenter%29.md)
  Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [class func pinAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint) -> Self](./pinattachment%28with,attachedto,attachmentanchor%29.md)
  Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [convenience init(item: any UIDynamicItem, attachedToAnchor: CGPoint)](./init%28item,attachedtoanchor%29.md)
  Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [convenience init(item: any UIDynamicItem, attachedTo: any UIDynamicItem)](./init%28item,attachedto%29.md)
  Initializes a behavior where the centers of two dynamic items are attached to each other.
- [init(item: any UIDynamicItem, offsetFromCenter: UIOffset, attachedToAnchor: CGPoint)](./init%28item,offsetfromcenter,attachedtoanchor%29.md)
  Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [init(item: any UIDynamicItem, offsetFromCenter: UIOffset, attachedTo: any UIDynamicItem, offsetFromCenter: UIOffset)](./init%28item,offsetfromcenter,attachedto,offsetfromcenter%29.md)
  Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/slidingattachment(with:attachedto:attachmentanchor:axisoftranslation:))*