# highlightedBranchImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default image for branch browser cells that are highlighted.

**Availability**:
- macOS

## Declaration

```swift
class var highlightedBranchImage: NSImage? { get }
```

```objc
@property (class, strong, readonly, nullable) NSImage * highlightedBranchImage;
```

## Return Value

The default image used for branch `NSBrowserCell` objects that are highlighted. This is a lighter version of the image returned by [`branchImage`](./branchimage.md).

## Discussion

Override this method if you want a different image.

## See Also

### Related Documentation
- [var alternateImage: NSImage?](./alternateimage.md)
  The browser cell’s image for the highlighted state.
### Getting Browser Cell Information
- [class var branchImage: NSImage?](./branchimage.md)
  Returns the default image for branch cells in a browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/highlightedbranchimage)*