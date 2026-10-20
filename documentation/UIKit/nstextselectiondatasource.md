# NSTextSelectionDataSource

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that objects implement to provide data for, and manage text selections.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextSelectionDataSource : NSObjectProtocol
```

```objc
@protocol NSTextSelectionDataSource <NSObject>
```

## Topics

### Range of the selection
- [var documentRange: NSTextRange](./nstextselectiondatasource/documentrange.md)
  Returns the starting and ending locations for the document.
### Enumerating components of the selection
- [func enumerateCaretOffsetsInLineFragment(at: any NSTextLocation, using: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./nstextselectiondatasource/enumeratecaretoffsetsinlinefragment%28at,using%29.md)
  Enumerates all the insertion point caret offsets from left to right in visual order.
- [func enumerateContainerBoundaries(from: any NSTextLocation, reverse: Bool, using: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)](./nstextselectiondatasource/enumeratecontainerboundaries%28from,reverse,using%29.md)
  Enumerates all the container boundaries starting from the location you specify.
- [func enumerateSubstrings(from: any NSTextLocation, options: NSString.EnumerationOptions, using: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)](./nstextselectiondatasource/enumeratesubstrings%28from,options,using%29.md)
  Enumerates the textual segment boundaries starting at the location you specify.
### Finding specific content in the selection
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](./nstextselectiondatasource/location%28_,offsetby%29.md)
  Returns a new location using the location and offset you specify.
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](./nstextselectiondatasource/linefragmentrange%28for,incontainerat%29.md)
  Returns the range of the line fragment that contains the point you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](./nstextselectiondatasource/offset%28from,to%29.md)
  Returns the offset between the two locations you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](./nstextselectiondatasource/textrange%28for,enclosing%29.md)
  Returns a text range that corresponds to selection granularity of the enclosing location.
### Changing the characteristics of the selection
- [func baseWritingDirection(at: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection](./nstextselectiondatasource/basewritingdirection%28at%29.md)
  Returns the base writing direction at the location you specify.
- [NSTextSelectionNavigation.WritingDirection](./nstextselectionnavigation/writingdirection.md)
  Values that describe the writing direction inside a text selection.
- [func textLayoutOrientation(at: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation](./nstextselectiondatasource/textlayoutorientation%28at%29.md)
  Returns the layout orientation at the location you specify.
- [NSTextSelectionNavigation.LayoutOrientation](./nstextselectionnavigation/layoutorientation.md)
  Values that describe the possible layout orientations.
### Instance Methods
- [func convertInteractionPoint(CGPoint, toContainerAt: any NSTextLocation) -> CGPoint](./nstextselectiondatasource/convertinteractionpoint%28_,tocontainerat%29.md)
  Converts an interaction point from display space into the text container’s coordinate system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTextLayoutManager](./nstextlayoutmanager.md)

## See Also

### Accessing the data source
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](./nstextselectionnavigation/textselectiondatasource.md)
  The data source associated with this selection navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource)*