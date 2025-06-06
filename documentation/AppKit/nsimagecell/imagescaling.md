# imageScaling

**Framework**: AppKit  
**Kind**: property

The scaling mode used to fit the receiver’s image into the frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var imageScaling: NSImageScaling { get set }
```

#### Discussion

For a list of possible values, see [`NSImageScaling`](nsimagescaling.md). The default value is [`NSImageScaling.scaleProportionallyDown`](nsimagescaling/scaleproportionallydown.md).

## See Also

- [var imageAlignment: NSImageAlignment](nsimagecell/imagealignment.md)
  The alignment of the receiver’s image relative to its frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagecell/imagescaling)*