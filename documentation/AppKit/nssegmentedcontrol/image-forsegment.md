# image(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the image associated with the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func image(forSegment segment: Int) -> NSImage?
```

#### Return Value

The image associated with the segment; otherwise, `nil`.

## Parameters

- `segment`: The index of the segment whose image you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setImage(NSImage?, forSegment: Int)](nssegmentedcontrol/setimage(_:forsegment:).md)
  Sets the image for the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](nssegmentedcontrol/setimagescaling(_:forsegment:).md)
  Sets the scaling mode used to display the specified segment’s image.
- [func imageScaling(forSegment: Int) -> NSImageScaling](nssegmentedcontrol/imagescaling(forsegment:).md)
  Returns the scaling mode used to display the specified segment’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/image(forsegment:))*