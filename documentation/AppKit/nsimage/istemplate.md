# isTemplate

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the image represents a template image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isTemplate: Bool { get set }
```

#### Discussion

Images you mark as template images should consist of only black and clear colors. You can use the alpha channel in the image to adjust the opacity of black content, however.

Template images are not intended to be used as standalone images. They are always mixed with other content and processed to create the desired appearance. You can mark an image as a “template image” to notify clients who care that the image contains only black and clear content. The most common use for template images is in image cells. For example, you might use a template image to provide the content for a button or segmented control. Cocoa cells take advantage of the nature of template images—that is, their simplified color scheme and use of transparency—to improve the appearance of the corresponding control in each of its supported states.

## See Also

- [var size: NSSize](nsimage/size.md)
  The size of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/istemplate)*