# highlightedBranchImage

**Framework**: AppKit  
**Kind**: property

Returns the default image for branch browser cells that are highlighted.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var highlightedBranchImage: NSImage? { get }
```

#### Return Value

The default image used for branch `NSBrowserCell` objects that are highlighted. This is a lighter version of the image returned by [`branchImage`](nsbrowsercell/branchimage.md).

#### Discussion

Override this method if you want a different image.

## See Also

- [var alternateImage: NSImage?](nsbrowsercell/alternateimage.md)
  The browser cell’s image for the highlighted state.
- [class var branchImage: NSImage?](nsbrowsercell/branchimage.md)
  Returns the default image for branch cells in a browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/highlightedbranchimage)*