# imageAlignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the receiver’s image relative to its frame.

**Availability**:
- macOS

## Declaration

```swift
var imageAlignment: NSImageAlignment { get set }
```

```objc
@property NSImageAlignment imageAlignment;
```

## Discussion

For a list of possible values, see [`NSImageAlignment`](../nsimagealignment.md). The default value is `NSImageAlignCenter`.

## See Also

### Related Documentation
- [class NSImageCell](../nsimagecell.md)
  An `NSImageCell` object displays a single image (encapsulated in an [`NSImage`](../nsimage.md) object) in a frame. This class provides methods for choosing the frame and for aligning and scaling the image to fit the frame.
### Aligning and Scaling the Image
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode used to fit the receiver’s image into the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagecell/imagealignment)*