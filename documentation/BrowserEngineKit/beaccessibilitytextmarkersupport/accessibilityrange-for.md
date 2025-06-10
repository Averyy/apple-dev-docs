# accessibilityRange(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns the range for the text in a given accessibility marker range.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func accessibilityRange(for range: BEAccessibilityTextMarker.Range) -> NSRange
```

#### Return Value

The range in the string for the text in `range`, or `(NSNotFound,0)` if the method can’t calculate the range.

## Parameters

- `range`: A text marker range for text in the element’s string.

## See Also

- [func accessibilityBounds(for: BEAccessibilityTextMarker.Range) -> CGRect](beaccessibilitytextmarkersupport/accessibilitybounds(for:).md)
  Calculates the bounding rectangle for a text range.
- [func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range](beaccessibilitytextmarkersupport/accessibilitytextmarkerrange.md)
  The text marker range of the current element.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](beaccessibilitytextmarkersupport/accessibilitytextmarkerrangeforcurrentselection.md)
  The text marker range of the current selection.
- [func accessibilityTextMarkerRange(for: NSRange) -> BEAccessibilityTextMarker.Range?](beaccessibilitytextmarkersupport/accessibilitytextmarkerrange(for:).md)
  Returns the text marker range for the text in a given range.
- [BEAccessibilityTextMarker.Range](beaccessibilitytextmarker/range.md)
  A class that represents a range in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilityrange(for:))*