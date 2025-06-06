# branchImage

**Framework**: AppKit  
**Kind**: property

Returns the default image for branch cells in a browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var branchImage: NSImage? { get }
```

#### Return Value

The default image used for branch `NSBrowserCell` objects. The default image is a right-pointing triangle.

#### Discussion

Override this method if you want a different image. To have a branch `NSBrowserCell` with no image (and no space reserved for an image), override this method to return `nil`.

## See Also

- [Browser Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Browser/Browser.html#//apple_ref/doc/uid/10000018i)
- [var alternateImage: NSImage?](nsbrowsercell/alternateimage.md)
  The browser cell’s image for the highlighted state.
- [class var highlightedBranchImage: NSImage?](nsbrowsercell/highlightedbranchimage.md)
  Returns the default image for branch browser cells that are highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/branchimage)*