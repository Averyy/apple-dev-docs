# NSTextLocation

**Framework**: UIKit  
**Kind**: protocol

An interface you implement that represents an abstract location inside your document’s content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol NSTextLocation : NSObjectProtocol
```

## Topics

### Comparing text locations
- [func compare(any NSTextLocation) -> ComparisonResult](nstextlocation/compare(_:).md)
  Compares and returns the logical ordering to location.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTextRange](nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelection](nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [class NSTextSelectionNavigation](nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlocation)*