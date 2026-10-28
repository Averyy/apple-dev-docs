# accessibilityTextMarkerRange(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text marker range for the text in a given range.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func accessibilityTextMarkerRange(for range: NSRange) -> BEAccessibilityTextMarker.Range?
```

```objc
- (BEAccessibilityTextMarkerRange *) accessibilityTextMarkerRangeForRange:(NSRange) range;
```

## Return Value

The text marker range for the text in `range`, or `nil` if the method can’t calculate the range.

## Parameters

- `range`: A range of text in the element’s string.

## See Also

### Text ranges
- [func accessibilityBounds(for: BEAccessibilityTextMarker.Range) -> CGRect](./accessibilitybounds%28for%29.md)
  Calculates the bounding rectangle for a text range.
- [func accessibilityTextMarkerRange() -> BEAccessibilityTextMarker.Range](./accessibilitytextmarkerrange%28%29.md)
  The text marker range of the current element.
- [func accessibilityTextMarkerRangeForCurrentSelection() -> BEAccessibilityTextMarker.Range?](./accessibilitytextmarkerrangeforcurrentselection%28%29.md)
  The text marker range of the current selection.
- [func accessibilityRange(for: BEAccessibilityTextMarker.Range) -> NSRange](./accessibilityrange%28for%29.md)
  Returns the range for the text in a given accessibility marker range.
- [BEAccessibilityTextMarker.Range](../beaccessibilitytextmarker/range.md)
  A class that represents a range in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitytextmarkerrange(for:))*