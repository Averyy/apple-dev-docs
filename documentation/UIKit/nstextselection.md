# NSTextSelection

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A class that represents a single logical selection context that corresponds to an insertion point.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextSelection
```

```objc
@interface NSTextSelection : NSObject
```

## Topics

### Creating a text selection
- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](./nstextselection/init%28_,affinity%29.md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./nstextselection/init%28range,affinity,granularity%29.md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./nstextselection/init%28_,affinity,granularity%29.md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](./nstextselection/init%28coder%29.md)
  Creates a test selection from data in an unarchiver.
### Characteristics of a selection
- [var affinity: NSTextSelection.Affinity](./nstextselection/affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](./nstextselection/affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](./nstextselection/anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [var granularity: NSTextSelection.Granularity](./nstextselection/granularity-swift.property.md)
  The granularity of the selection.
- [NSTextSelection.Granularity](./nstextselection/granularity-swift.enum.md)
  Values that describe the different granularities available to make a selection.
- [var isLogical: Bool](./nstextselection/islogical.md)
  A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [var isTransient: Bool](./nstextselection/istransient.md)
  A Boolean value that indicates transient text selection during drag handling.
- [var secondarySelectionLocation: (any NSTextLocation)?](./nstextselection/secondaryselectionlocation.md)
  Specifies the secondary character location when user taps or clicks at a directional boundary.
- [protocol NSTextLocation](./nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
- [var textRanges: [NSTextRange]](./nstextselection/textranges.md)
  Represents an array of noncontiguous logical ranges in the selection.
- [var typingAttributes: [NSAttributedString.Key : Any]](./nstextselection/typingattributes.md)
  The template attributes the framework uses for characters that replace the contents of this selection.
### Creating subselections
- [func textSelection([NSTextRange]) -> NSTextSelection](./nstextselection/textselection%28_%29.md)
  Creates a subselection of the current text selection with the ranges you specify.
### Initializers
- [convenience init(location: any NSTextLocation, affinity: NSTextSelection.Affinity)](./nstextselection/init%28location,affinity%29.md)
- [init(ranges: [NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./nstextselection/init%28ranges,affinity,granularity%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Location and selection
- [class NSTextRange](./nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelectionNavigation](./nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [protocol NSTextLocation](./nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection)*