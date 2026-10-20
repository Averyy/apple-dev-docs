# fixedAttachment(with:attachedTo:attachmentAnchor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func fixedAttachment(with item1: any UIDynamicItem, attachedTo item2: any UIDynamicItem, attachmentAnchor point: CGPoint) -> Self
```

```objc
+ (instancetype) fixedAttachmentWithItem:(id<UIDynamicItem>) item1 attachedToItem:(id<UIDynamicItem>) item2 attachmentAnchor:(CGPoint) point;
```

#### Return Value

A new attachment object or `nil` if the object could not be created.

#### Discussion

The behavior created by this method acts like a solid rod connecting each item to the specified anchor point. The position of the items relative to each other does not change. Forces acting on the items move them together as if they were a single unit.

## Parameters

- `item1`: The first of two dynamic items connected by the attachment behavior.
- `item2`: The second of two dynamic items connected by the attachment behavior.
- `point`: The anchor point for both items. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see [`UIDynamicAnimator`](../uidynamicanimator.md).

## See Also

### Creating and initializing attachment behavior objects
- [class func slidingAttachment(with: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](./slidingattachment%28with,attachmentanchor,axisoftranslation%29.md)
  Creates and returns an attachment behavior where one item slides along the specified axis.
- [class func slidingAttachment(with: any UIDynamicItem, attachedTo: any UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self](./slidingattachment%28with,attachedto,attachmentanchor,axisoftranslation%29.md)
  Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/fixedattachment(with:attachedto:attachmentanchor:))*