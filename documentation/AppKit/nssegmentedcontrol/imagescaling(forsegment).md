# imageScaling(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the scaling mode used to display the specified segment’s image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func imageScaling(forSegment segment: Int) -> NSImageScaling
```

```objc
- (NSImageScaling) imageScalingForSegment:(NSInteger) segment;
```

#### Return Value

One of the image scaling constants. For a list of possible values, see [`NSImageScaling`](../nsimagescaling.md). The default value is [`NSImageScaling.scaleProportionallyDown`](../nsimagescaling/scaleproportionallydown.md).

## Parameters

- `segment`: The index of the segment whose enabled state you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring a segment image
- [func setImage(NSImage?, forSegment: Int)](./setimage%28_,forsegment%29.md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](./image%28forsegment%29.md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](./setimagescaling%28_,forsegment%29.md)
  Sets the scaling mode used to display the specified segment’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/imagescaling(forsegment:))*