# accessibilityBounds(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calculates the bounding rectangle for a text range.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func accessibilityBounds(for range: BEAccessibilityTextMarker.Range) -> CGRect
```

```objc
- (CGRect) accessibilityBoundsForTextMarkerRange:(BEAccessibilityTextMarkerRange *) range;
```

## Return Value

The bounds in accessiblity space of the text range, or [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if the method can’t calculate the bounds.

## Parameters

- `range`: The text marker range.

## See Also

### Text ranges
- [func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range](./accessibilitytextmarkerrange%28%29.md)
  The text marker range of the current element.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](./accessibilitytextmarkerrangeforcurrentselection%28%29.md)
  The text marker range of the current selection.
- [func accessibilityTextMarkerRange(for: NSRange) -> BEAccessibilityTextMarker.Range?](./accessibilitytextmarkerrange%28for%29.md)
  Returns the text marker range for the text in a given range.
- [func accessibilityRange(for: BEAccessibilityTextMarker.Range) -> NSRange](./accessibilityrange%28for%29.md)
  Returns the range for the text in a given accessibility marker range.
- [BEAccessibilityTextMarker.Range](../beaccessibilitytextmarker/range.md)
  A class that represents a range in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitybounds(for:))*