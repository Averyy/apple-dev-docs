# image(forBounds:textContainer:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the image object that the layout manager renders in the specified image bounds rectangle inside the text container.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func image(forBounds imageBounds: CGRect, textContainer: NSTextContainer?, characterIndex charIndex: Int) -> NSImage?
```

#### Return Value

The image rendered in the bounds rectangle.

#### Discussion

The method should return an image appropriate for the target rendering context derived by arguments passed into this method. The `NSTextAttachment` implementation returns the text attachment’s [`image`](nstextattachment/image.md) when non-`nil`. If the image is `nil`, it returns an image based on the text attachment’s [`contents`](nstextattachment/contents.md) and [`fileType`](nstextattachment/filetype.md) properties.

## Parameters

- `imageBounds`: The rectangle in which the image is laid out.
- `textContainer`: The text container in which the image is laid out.
- `charIndex`: The character location inside the text storage for the attachment character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer/image(forbounds:textcontainer:characterindex:))*