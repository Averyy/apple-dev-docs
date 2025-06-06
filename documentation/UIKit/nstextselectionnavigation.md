# NSTextSelectionNavigation

**Framework**: UIKit  
**Kind**: class

An interface you use to expose methods for obtaining results from actions performed on text selections.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextSelectionNavigation
```

## Topics

### Creating a selection navigation
- [init(dataSource: any NSTextSelectionDataSource)](nstextselectionnavigation/init(datasource:).md)
  Creates a new object using the text selection data source you provide.
### Selection characteristics
- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](nstextselectionnavigation/destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](nstextselectionnavigation/direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](nstextselectionnavigation/textselection(for:enclosing:incontainerat:).md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.
### Accessing the data source
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](nstextselectionnavigation/textselectiondatasource.md)
  The data source associated with this selection navigation.
- [protocol NSTextSelectionDataSource](nstextselectiondatasource.md)
  A set of methods that objects implement to provide data for, and manage text selections.
### Working with text selections
- [func textSelection(for: NSTextSelection.Granularity, enclosing: NSTextSelection) -> NSTextSelection](nstextselectionnavigation/textselection(for:enclosing:).md)
  Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [func textSelections(interactingAt: CGPoint, inContainerAt: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]](nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:).md)
  Returns an array of text selections produced by a tap or click at the point you specify.
- [func destinationSelection(for: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?](nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:).md)
  Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.
### Controlling cache behavior
- [func flushLayoutCache()](nstextselectionnavigation/flushlayoutcache.md)
  Flushes cached layout information.
### Finding the insertion point
- [func resolvedInsertionLocation(for: NSTextSelection, writingDirection: NSTextSelectionNavigation.WritingDirection) -> (any NSTextLocation)?](nstextselectionnavigation/resolvedinsertionlocation(for:writingdirection:).md)
  Returns the location for inserting the next input depending on the state of the current and secondary selections.
### Specifying deletion ranges
- [func deletionRanges(for: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, allowsDecomposition: Bool) -> [NSTextRange]](nstextselectionnavigation/deletionranges(for:direction:destination:allowsdecomposition:).md)
  Returns the ranges for deleting the text based on the current selection and movement arguments.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTextRange](nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelection](nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation)*