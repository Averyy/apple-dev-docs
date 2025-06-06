# setImage(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the image for the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setImage(_ image: NSImage?, forSegment segment: Int)
```

## Parameters

- `image`: The image to apply to the segment or   if you want to clear the existing image. Images are not scaled to fit inside a segment. If the image is larger than the available space, it is clipped.
- `segment`: The index of the segment whose image you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func image(forSegment: Int) -> NSImage?](nssegmentedcontrol/image(forsegment:).md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](nssegmentedcontrol/setimagescaling(_:forsegment:).md)
  Sets the scaling mode used to display the specified segment’s image.
- [func imageScaling(forSegment: Int) -> NSImageScaling](nssegmentedcontrol/imagescaling(forsegment:).md)
  Returns the scaling mode used to display the specified segment’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setimage(_:forsegment:))*