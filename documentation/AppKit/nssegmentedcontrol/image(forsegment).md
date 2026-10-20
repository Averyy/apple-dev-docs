# image(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the image associated with the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func image(forSegment segment: Int) -> NSImage?
```

```objc
- (NSImage *) imageForSegment:(NSInteger) segment;
```

#### Return Value

The image associated with the segment; otherwise, `nil`.

## Parameters

- `segment`: The index of the segment whose image you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring a segment image
- [func setImage(NSImage?, forSegment: Int)](./setimage%28_,forsegment%29.md)
  Sets the image for the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](./setimagescaling%28_,forsegment%29.md)
  Sets the scaling mode used to display the specified segment’s image.
- [func imageScaling(forSegment: Int) -> NSImageScaling](./imagescaling%28forsegment%29.md)
  Returns the scaling mode used to display the specified segment’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/image(forsegment:))*