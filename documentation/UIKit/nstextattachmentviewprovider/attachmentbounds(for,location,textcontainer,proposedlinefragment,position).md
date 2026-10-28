# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the layout bounds for an attachment at a specific text location that contains the text attributes you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

```objc
- (CGRect) attachmentBoundsForAttributes:(NSDictionary<NSString *,id> *) attributes location:(id<NSTextLocation>) location textContainer:(NSTextContainer *) textContainer proposedLineFragment:(CGRect) proposedLineFragment position:(CGPoint) position;
```

## Return Value

Returns a [`CGRect`](../../CoreFoundation/cgrect.md) that describes the bounds of the attachment.

## Parameters

- `attributes`: A dictionary that contains a list of key and attribute pairs that describe the customization of the string.
- `location`: An [`NSTextLocation`](../nstextlocation.md) that indicates that start of the string.
- `textContainer`: The [`NSTextContainer`](../nstextcontainer.md) that contains the source string.
- `proposedLineFragment`: A [`CGRect`](../../CoreFoundation/cgrect.md) that describes the boundaries of the line fragment.
- `position`: A [`CGPoint`](../../CoreFoundation/cgpoint.md) inside `proposedLineFragment`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:))*