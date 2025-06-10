# BEAccessibilityTextMarker

**Framework**: BrowserEngineKit  
**Kind**: class

An abstract class that represents a location in an element’s accessibility text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
class BEAccessibilityTextMarker
```

#### Overview

Subclass `BEAccessibilityTextMarker` in your app to represent a location in the accessibility text of an element in the document object model (DOM). The system uses your implementation of [`BEAccessibilityTextMarkerSupport`](beaccessibilitytextmarkersupport.md) to convert between accessibility text markers and locations in your app’s views, and doesn’t create instances of your subclass or access their data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func accessibilityNextTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitynexttextmarker(_:).md)
  Returns the text marker that follows the given text marker.
- [func accessibilityPreviousTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilityprevioustextmarker(_:).md)
  Returns the text marker that precedes the given text marker.
- [func accessibilityLineStartMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitylinestartmarker(for:).md)
  Returns the text marker that represents the start of the line that contains the given text marker.
- [func accessibilityLineEndMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitylineendmarker(for:).md)
  Returns the text marker that represents the end of the line that contains the given text marker.
- [func accessibilityMarker(for: CGPoint) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitymarker(for:).md)
  Returns the text marker at a point in the view’s coordinate system.
- [func accessibilityTextMarker(forPosition: Int) -> BEAccessibilityTextMarker?](beaccessibilitytextmarkersupport/accessibilitytextmarker(forposition:).md)
  Returns the text marker for the text at a given index in the element’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarker)*