# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

**Framework**: AppKit  
**Kind**: method

Returns the layout bounds for an attachment at a specific text location that contains the text attributes you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

#### Return Value

Returns a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) that describes the bounds of the attachment.

## Parameters

- `attributes`: A dictionary that contains a list of key and attribute pairs that describe the customization of the string.
- `location`: An   that indicates that start of the string.
- `textContainer`: The   that contains the source string.
- `proposedLineFragment`: A   that describes the boundaries of the line fragment.
- `position`: A   inside  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentviewprovider/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:))*