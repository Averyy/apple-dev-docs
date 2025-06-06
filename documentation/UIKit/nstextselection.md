# NSTextSelection

**Framework**: UIKit  
**Kind**: class

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

## Topics

### Creating a text selection
- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](nstextselection/init(_:affinity:).md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(range:affinity:granularity:).md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(_:affinity:granularity:).md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](nstextselection/init(coder:).md)
  Creates a test selection from data in an unarchiver.
### Characteristics of a selection
- [var affinity: NSTextSelection.Affinity](nstextselection/affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](nstextselection/affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](nstextselection/anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [var granularity: NSTextSelection.Granularity](nstextselection/granularity-swift.property.md)
  The granularity of the selection.
- [NSTextSelection.Granularity](nstextselection/granularity-swift.enum.md)
  Values that describe the different granularities available to make a selection.
- [var isLogical: Bool](nstextselection/islogical.md)
  A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [var isTransient: Bool](nstextselection/istransient.md)
  A Boolean value that indicates transient text selection during drag handling.
- [var secondarySelectionLocation: (any NSTextLocation)?](nstextselection/secondaryselectionlocation.md)
  Specifies the secondary character location when user taps or clicks at a directional boundary.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
- [var textRanges: [NSTextRange]](nstextselection/textranges.md)
  Represents an array of noncontiguous logical ranges in the selection.
- [var typingAttributes: [NSAttributedString.Key : Any]](nstextselection/typingattributes.md)
  The template attributes the framework uses for characters that replace the contents of this selection.
### Creating subselections
- [func textSelection([NSTextRange]) -> NSTextSelection](nstextselection/textselection(_:).md)
  Creates a subselection of the current text selection with the ranges you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSTextRange](nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelectionNavigation](nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection)*