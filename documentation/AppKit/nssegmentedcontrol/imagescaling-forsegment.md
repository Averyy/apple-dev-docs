# imageScaling(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the scaling mode used to display the specified segment’s image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func imageScaling(forSegment segment: Int) -> NSImageScaling
```

#### Return Value

One of the image scaling constants. For a list of possible values, see [`NSImageScaling`](nsimagescaling.md). The default value is [`NSImageScaling.scaleProportionallyDown`](nsimagescaling/scaleproportionallydown.md).

## Parameters

- `segment`: The index of the segment whose enabled state you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setImage(NSImage?, forSegment: Int)](nssegmentedcontrol/setimage(_:forsegment:).md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](nssegmentedcontrol/image(forsegment:).md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](nssegmentedcontrol/setimagescaling(_:forsegment:).md)
  Sets the scaling mode used to display the specified segment’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/imagescaling(forsegment:))*