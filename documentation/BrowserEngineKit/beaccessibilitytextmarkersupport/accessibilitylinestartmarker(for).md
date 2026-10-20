# accessibilityLineStartMarker(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text marker that represents the start of the line that contains the given text marker.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func accessibilityLineStartMarker(for marker: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?
```

```objc
- (BEAccessibilityTextMarker *) accessibilityLineStartMarkerForMarker:(BEAccessibilityTextMarker *) marker;
```

#### Return Value

A text marker that represents the start of the line that contains `marker`, or `nil` if there isn’t one.

## Parameters

- `marker`: A text marker.

## See Also

### Text positions
- [func accessibilityNextTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./accessibilitynexttextmarker%28_%29.md)
  Returns the text marker that follows the given text marker.
- [func accessibilityPreviousTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./accessibilityprevioustextmarker%28_%29.md)
  Returns the text marker that precedes the given text marker.
- [func accessibilityLineEndMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./accessibilitylineendmarker%28for%29.md)
  Returns the text marker that represents the end of the line that contains the given text marker.
- [func accessibilityMarker(for: CGPoint) -> BEAccessibilityTextMarker?](./accessibilitymarker%28for%29.md)
  Returns the text marker at a point in the view’s coordinate system.
- [func accessibilityTextMarker(forPosition: Int) -> BEAccessibilityTextMarker?](./accessibilitytextmarker%28forposition%29.md)
  Returns the text marker for the text at a given index in the element’s text.
- [class BEAccessibilityTextMarker](../beaccessibilitytextmarker.md)
  An abstract class that represents a location in an element’s accessibility text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitylinestartmarker(for:))*