# accessibilityMarker(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns the text marker at a point in the view’s coordinate system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func accessibilityMarker(for point: CGPoint) -> BEAccessibilityTextMarker?
```

#### Return Value

The text marker for the text at `point`, or `nil` if there isn’t text at that point.

## Parameters

- `point`: A location in the view’s bounds.

## See Also

- [func accessibilityNextTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitynexttextmarker(_:).md)
  Returns the text marker that follows the given text marker.
- [func accessibilityPreviousTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilityprevioustextmarker(_:).md)
  Returns the text marker that precedes the given text marker.
- [func accessibilityLineStartMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitylinestartmarker(for:).md)
  Returns the text marker that represents the start of the line that contains the given text marker.
- [func accessibilityLineEndMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitylineendmarker(for:).md)
  Returns the text marker that represents the end of the line that contains the given text marker.
- [func accessibilityTextMarker(forPosition: Int) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitytextmarker(forposition:).md)
  Returns the text marker for the text at a given index in the element’s text.
- [class BEAccessibilityTextMarker](beaccessibilitytextmarker.md)
  An abstract class that represents a location in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitymarker(for:))*