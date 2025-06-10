# NSBrowserCell

**Framework**: AppKit  
**Kind**: class

The user interface of a browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSBrowserCell
```

#### Overview

The [`NSBrowserCell`](nsbrowsercell.md) class is the subclass of [`NSCell`](nscell.md) used by default to display data in the columns of an [`NSBrowser`](nsbrowser.md) object. (Each column contains an [`NSMatrix`](nsmatrix.md) object filled with [`NSBrowserCell`](nsbrowsercell.md) objects.)

## Topics

### Getting Browser Cell Information
- [class var branchImage: NSImage?](nsbrowsercell/branchimage.md)
  Returns the default image for branch cells in a browser.
- [class var highlightedBranchImage: NSImage?](nsbrowsercell/highlightedbranchimage.md)
  Returns the default image for branch browser cells that are highlighted.
### Configuring Browser Cells
- [var image: NSImage?](nsbrowsercell/image.md)
  The browser cell’s image.
- [var alternateImage: NSImage?](nsbrowsercell/alternateimage.md)
  The browser cell’s image for the highlighted state.
### Managing Browser Cell State
- [func reset()](nsbrowsercell/reset.md)
  Unhighlights the receiver and unsets its state.
- [func set()](nsbrowsercell/set.md)
  Highlights the receiver and sets its state.
- [var isLeaf: Bool](nsbrowsercell/isleaf.md)
  A Boolean that indicates whether the browser cell is a leaf or a branch cell.
- [var isLoaded: Bool](nsbrowsercell/isloaded.md)
  A Boolean that indicates whether the cell is ready to display.
- [func highlightColor(in: NSView) -> NSColor?](nsbrowsercell/highlightcolor(in:).md)
  Returns the highlight color that the receiver wants to display.
### Initializers
- [init(coder: NSCoder)](nsbrowsercell/init(coder:).md)
- [init(imageCell: NSImage?)](nsbrowsercell/init(imagecell:).md)
- [init(textCell: String)](nsbrowsercell/init(textcell:).md)

## Relationships

### Inherits From
- [NSCell](nscell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell)*