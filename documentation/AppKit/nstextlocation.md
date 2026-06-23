# NSTextLocation

**Framework**: AppKit  
**Kind**: protocol

An interface you implement that represents an abstract location inside your document’s content.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextLocation : NSObjectProtocol
```

## Topics

### Comparing text locations
- [func compare(any NSTextLocation) -> ComparisonResult](nstextlocation/compare(_:).md)
  Compares and returns the logical ordering to location.
### Instance Properties
- [var hash: Int](nstextlocation/hash.md)
  Must be consistent with results from `isEqual:` while also avoiding hash collisions.
### Instance Methods
- [func isEqual(Any?) -> Bool](nstextlocation/isequal(_:).md)
  Returns `true` for locations representing the same document position.

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
- [class NSTextSelectionManager](nstextselectionmanager.md)
  An object that coordinates text selection behavior for custom text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlocation)*