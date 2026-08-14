# BEAccessibilityTextMarker.Range

**Framework**: BrowserEngineKit  
**Kind**: class

A class that represents a range in an element’s accessibility text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
class Range
```

## Topics

### Range boundaries
- [var startMarker: BEAccessibilityTextMarker](beaccessibilitytextmarker/range/startmarker.md)
  The marker at the beginning of a range in an element’s accessibility text.
- [var endMarker: BEAccessibilityTextMarker](beaccessibilitytextmarker/range/endmarker.md)
  The marker at the end of a range in an element’s accessibility text.
### Initializers
- [init?(coder: NSCoder)](beaccessibilitytextmarker/range/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func accessibilityBounds(for: BEAccessibilityTextMarker.Range) -> CGRect](beaccessibilitytextmarkersupport/accessibilitybounds(for:).md)
  Calculates the bounding rectangle for a text range.
- [func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range](beaccessibilitytextmarkersupport/accessibilitytextmarkerrange.md)
  The text marker range of the current element.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](beaccessibilitytextmarkersupport/accessibilitytextmarkerrangeforcurrentselection.md)
  The text marker range of the current selection.
- [func accessibilityTextMarkerRange(for: NSRange) -> BEAccessibilityTextMarker.Range?](beaccessibilitytextmarkersupport/accessibilitytextmarkerrange(for:).md)
  Returns the text marker range for the text in a given range.
- [func accessibilityRange(for: BEAccessibilityTextMarker.Range) -> NSRange](beaccessibilitytextmarkersupport/accessibilityrange(for:).md)
  Returns the range for the text in a given accessibility marker range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarker/range)*