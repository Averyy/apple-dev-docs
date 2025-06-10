# BEAccessibilityTextMarkerSupport

**Framework**: BrowserEngineKit  
**Kind**: protocol

A set of methods that provide information about text offsets to support assistive features.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
protocol BEAccessibilityTextMarkerSupport : NSObjectProtocol
```

#### Overview

In your alternative browser engine, implement `BEAccessibilityTextMarkerSupport` on views that represent elements in the Document Object Model (DOM) to supply accessibility information about the element’s text to the system.

## Topics

### Text positions
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
- [class BEAccessibilityTextMarker](beaccessibilitytextmarker.md)
  An abstract class that represents a location in an element’s accessibility text.
### Text ranges
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
- [BEAccessibilityTextMarker.Range](beaccessibilitytextmarker/range.md)
  A class that represents a range in an element’s accessibility text.
### Instance Methods
- [func accessibilityContent(for: BEAccessibilityTextMarker.Range) -> String?](beaccessibilitytextmarkersupport/accessibilitycontent(for:).md)
  Returns the accessibility content for a text range.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  The notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  The notification you post when the selection inside an element changes.
- [struct BEAccessibilityContainerType](beaccessibilitycontainertype.md)
  An enumeration that indicates the type of container in which an element is located.
- [enum BEAccessibilityPressedState](beaccessibilitypressedstate.md)
  An enumeration that indicates whether an element is pressed.
- [static var menuItem: UIAccessibilityTraits](beaccessibility/menuitem.md)
  The accessibility element behaves like a menu item.
- [static var popUpButton: UIAccessibilityTraits](beaccessibility/popupbutton.md)
  The accessibility element behaves like a pop-up button.
- [static var radioButton: UIAccessibilityTraits](beaccessibility/radiobutton.md)
  The accessibility element behaves like a radio button.
- [static var readOnly: UIAccessibilityTraits](beaccessibility/readonly.md)
  The accessibility element is read-only.
- [static var visited: UIAccessibilityTraits](beaccessibility/visited.md)
  The accessibility element behaves like a link that someone previously visited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport)*