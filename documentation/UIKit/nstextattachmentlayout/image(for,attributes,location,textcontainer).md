# image(for:attributes:location:textContainer:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the image object rendered at the bounds and inside the text container you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func image(for bounds: CGRect, attributes: [NSAttributedString.Key : Any] = [:], location: any NSTextLocation, textContainer: NSTextContainer?) -> UIImage?
```

```objc
- (UIImage *) imageForBounds:(CGRect) bounds attributes:(NSDictionary<NSString *,id> *) attributes location:(id<NSTextLocation>) location textContainer:(NSTextContainer *) textContainer;
```

## Return Value

An optional image object.

## Discussion

A custom implementation should return an image appropriate for the target rendering context that you derive by arguments to this method. The default [`NSTextAttachment`](../nstextattachment.md) implementation returns the contents of the `image` property when non-`nil`. If the `image` property is `nil`, it returns an image based on the `contents` and `fileType` properties.

## Parameters

- `bounds`: The [`CGRect`](../../CoreFoundation/cgrect.md) that presents the image boundaries inside `textContainer`.
- `attributes`: A dictionary of [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) attributes.
- `location`: An [`NSTextLocation`](../nstextlocation.md) that indicates that start of the string.
- `textContainer`: The [`NSTextContainer`](../nstextcontainer.md) that contains the source text.

## See Also

### Determining the characteristics of an attachment
- [func attachmentBounds(for: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect](./attachmentbounds%28for,location,textcontainer,proposedlinefragment,position%29.md)
  Returns the layout bounds of the attachment you specify.
- [func viewProvider(for: UIView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?](./viewprovider%28for,location,textcontainer%29.md)
  Returns the text attachment view provider corresponding to the file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentlayout/image(for:attributes:location:textcontainer:))*