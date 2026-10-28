# branchImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default image for branch cells in a browser.

**Availability**:
- macOS

## Declaration

```swift
class var branchImage: NSImage? { get }
```

```objc
@property (class, strong, readonly, nullable) NSImage * branchImage;
```

## Return Value

The default image used for branch `NSBrowserCell` objects. The default image is a right-pointing triangle.

## Discussion

Override this method if you want a different image. To have a branch `NSBrowserCell` with no image (and no space reserved for an image), override this method to return `nil`.

## See Also

### Related Documentation
- [var alternateImage: NSImage?](./alternateimage.md)
  The browser cell’s image for the highlighted state.
### Getting Browser Cell Information
- [class var highlightedBranchImage: NSImage?](./highlightedbranchimage.md)
  Returns the default image for branch browser cells that are highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/branchimage)*