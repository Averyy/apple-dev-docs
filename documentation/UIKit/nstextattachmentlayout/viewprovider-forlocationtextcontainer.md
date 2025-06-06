# viewProvider(for:location:textContainer:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the text attachment view provider corresponding to the file type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func viewProvider(for parentView: UIView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?
```

#### Return Value

An [`NSTextAttachmentViewProvider`](nstextattachmentviewprovider.md).

#### Discussion

The default implementation queries the text attachment view provider class using the [`textAttachmentViewProviderClass(forFileType:)`](nstextattachment/textattachmentviewproviderclass(forfiletype:).md) method of [`NSTextAttachment`](nstextattachment.md). When non-`nil`, it instantiates a view, then, fills properties declared in `NSTextAttachmentViewProvider` if implemented.

## Parameters

- `parentView`: The parent view.
- `location`: An   that indicates that start of the string.
- `textContainer`: The   that contains the source text.

## See Also

- [func attachmentBounds(for: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect](nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:).md)
  Returns the layout bounds of the attachment you specify.
- [func image(for: CGRect, attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?) -> UIImage?](nstextattachmentlayout/image(for:attributes:location:textcontainer:).md)
  Returns the image object rendered at the bounds and inside the text container you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentlayout/viewprovider(for:location:textcontainer:))*