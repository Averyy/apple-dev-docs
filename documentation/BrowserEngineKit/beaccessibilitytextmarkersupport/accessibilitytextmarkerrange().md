# accessibilityTextMarkerRange()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The text marker range of the current element.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range
```

```objc
- (BEAccessibilityTextMarkerRange *) accessibilityTextMarkerRange;
```

## See Also

### Text ranges
- [func accessibilityBounds(for: BEAccessibilityTextMarker.Range) -> CGRect](./accessibilitybounds%28for%29.md)
  Calculates the bounding rectangle for a text range.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](./accessibilitytextmarkerrangeforcurrentselection%28%29.md)
  The text marker range of the current selection.
- [func accessibilityTextMarkerRange(for: NSRange) -> BEAccessibilityTextMarker.Range?](./accessibilitytextmarkerrange%28for%29.md)
  Returns the text marker range for the text in a given range.
- [func accessibilityRange(for: BEAccessibilityTextMarker.Range) -> NSRange](./accessibilityrange%28for%29.md)
  Returns the range for the text in a given accessibility marker range.
- [BEAccessibilityTextMarker.Range](../beaccessibilitytextmarker/range.md)
  A class that represents a range in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitytextmarkerrange())*