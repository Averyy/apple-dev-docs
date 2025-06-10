# accessibilityLineEndMarker(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns the text marker that represents the end of the line that contains the given text marker.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func accessibilityLineEndMarker(for marker: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?
```

#### Return Value

A text marker that represents the end of the line that contains `marker`, or `nil` if there isn’t one.

## Parameters

- `marker`: A text marker.

## See Also

- [func accessibilityNextTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitynexttextmarker(_:).md)
  Returns the text marker that follows the given text marker.
- [func accessibilityPreviousTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilityprevioustextmarker(_:).md)
  Returns the text marker that precedes the given text marker.
- [func accessibilityLineStartMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitylinestartmarker(for:).md)
  Returns the text marker that represents the start of the line that contains the given text marker.
- [func accessibilityMarker(for: CGPoint) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitymarker(for:).md)
  Returns the text marker at a point in the view’s coordinate system.
- [func accessibilityTextMarker(forPosition: Int) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitytextmarker(forposition:).md)
  Returns the text marker for the text at a given index in the element’s text.
- [class BEAccessibilityTextMarker](beaccessibilitytextmarker.md)
  An abstract class that represents a location in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitylineendmarker(for:))*