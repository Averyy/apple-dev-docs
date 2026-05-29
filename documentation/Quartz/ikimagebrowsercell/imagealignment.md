# imageAlignment()

**Framework**: Quartz  
**Kind**: method

Returns the position of the cell’s image in the frame.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func imageAlignment() -> NSImageAlignment
```

#### Return Value

The alignment of the image. See [`NSImageAlignment`](https://developer.apple.com/documentation/AppKit/NSImageAlignment) for possible values.

#### Discussion

Subclasses can override this method to customize the image alignment.

The image frame will be computed automatically from the image container frame by taking in account the image alignment and the image aspect ratio.

## See Also

- [func opacity() -> CGFloat](ikimagebrowsercell/opacity.md)
  Returns the opacity of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/imagealignment())*