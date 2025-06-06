# imageAlignment

**Framework**: AppKit  
**Kind**: property

The alignment of the image within the scrubber item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var imageAlignment: NSImageAlignment { get set }
```

#### Discussion

The image is scaled proportionally to fit the frame of the item. This property determines how the image is cropped within that frame.

For possible values, see [`NSImageAlignment`](nsimagealignment.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberimageitemview/imagealignment)*