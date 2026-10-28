# viewProvider(for:location:textContainer:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text attachment view provider corresponding to the file type.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func viewProvider(for parentView: NSView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?
```

```objc
- (NSTextAttachmentViewProvider *) viewProviderForParentView:(NSView *) parentView location:(id<NSTextLocation>) location textContainer:(NSTextContainer *) textContainer;
```

## Return Value

An [`NSTextAttachmentViewProvider`](../nstextattachmentviewprovider.md).

## Discussion

The default implementation queries the text attachment view provider class using the [`textAttachmentViewProviderClass(forFileType:)`](../nstextattachment/textattachmentviewproviderclass%28forfiletype%29.md) method of [`NSTextAttachment`](../nstextattachment.md). When non-`nil`, it instantiates a view, then, fills properties declared in `NSTextAttachmentViewProvider` if implemented.

## Parameters

- `parentView`: The parent view.
- `location`: An <[`NSTextLocation`](../nstextlocation.md) that indicates that start of the string.
- `textContainer`: The[`NSTextContainer`](../nstextcontainer.md) that contains the source text.

## See Also

### Determining the characteristics of an attachment
- [func attachmentBounds(for: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect](./attachmentbounds%28for,location,textcontainer,proposedlinefragment,position%29.md)
  Returns the layout bounds of the attachment you specify.
- [func image(for: CGRect, attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?) -> NSImage?](./image%28for,attributes,location,textcontainer%29.md)
  Returns the image object rendered at the bounds and inside the text container you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentlayout/viewprovider(for:location:textcontainer:))*