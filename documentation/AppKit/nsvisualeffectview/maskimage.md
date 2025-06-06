# maskImage

**Framework**: AppKit  
**Kind**: property

An image whose alpha channel masks the visual effect view’s material.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var maskImage: NSImage? { get set }
```

#### Discussion

The default value of this property is `nil`, which is the equivalent of allowing all of the visual effect view’s content to show through. Assigning an image to this property masks the portions of the visual effect view using the image’s alpha channel.

If the visual effect view is the content view of a window, the mask is applied in an appropriate way to the window’s shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/maskimage)*