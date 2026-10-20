# BEAccessibilityTextMarker.Range

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A class that represents a range in an element’s accessibility text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
class Range
```

```objc
@interface BEAccessibilityTextMarkerRange : NSObject
```

## Topics

### Range boundaries
- [var startMarker: BEAccessibilityTextMarker](./range/startmarker.md)
  The marker at the beginning of a range in an element’s accessibility text.
- [var endMarker: BEAccessibilityTextMarker](./range/endmarker.md)
  The marker at the end of a range in an element’s accessibility text.
### Initializers
- [init?(coder: NSCoder)](./range/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Text ranges
- [func accessibilityBounds(for: BEAccessibilityTextMarker.Range) -> CGRect](../beaccessibilitytextmarkersupport/accessibilitybounds%28for%29.md)
  Calculates the bounding rectangle for a text range.
- [func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range](../beaccessibilitytextmarkersupport/accessibilitytextmarkerrange%28%29.md)
  The text marker range of the current element.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](../beaccessibilitytextmarkersupport/accessibilitytextmarkerrangeforcurrentselection%28%29.md)
  The text marker range of the current selection.
- [func accessibilityTextMarkerRange(for: NSRange) -> BEAccessibilityTextMarker.Range?](../beaccessibilitytextmarkersupport/accessibilitytextmarkerrange%28for%29.md)
  Returns the text marker range for the text in a given range.
- [func accessibilityRange(for: BEAccessibilityTextMarker.Range) -> NSRange](../beaccessibilitytextmarkersupport/accessibilityrange%28for%29.md)
  Returns the range for the text in a given accessibility marker range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarker/range)*