# accessibilityScreenSize(forLayoutSize:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Converts the provided size in the layout area’s coordinates to a size in the screen’s coordinate system.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityScreenSize(forLayoutSize size: NSSize) -> NSSize
```

#### Return Value

A size in the screen’s coordinate system.

## Parameters

- `size`: A size in the layout area’s coordinate system.

## See Also

- [func accessibilityHandles() -> [Any]?](nsaccessibilityprotocol/accessibilityhandles.md)
  Returns the drag handle elements for the layout item element.
- [func setAccessibilityHandles([Any]?)](nsaccessibilityprotocol/setaccessibilityhandles(_:).md)
  Sets the drag handle accessibility elements for the layout item element.
- [func accessibilityHorizontalUnits() -> NSAccessibilityUnits](nsaccessibilityprotocol/accessibilityhorizontalunits.md)
  Returns the units that the layout area uses for horizontal values.
- [func setAccessibilityHorizontalUnits(NSAccessibilityUnits)](nsaccessibilityprotocol/setaccessibilityhorizontalunits(_:).md)
  Sets the units that the layout area uses for horizontal values.
- [func accessibilityHorizontalUnitDescription() -> String?](nsaccessibilityprotocol/accessibilityhorizontalunitdescription.md)
  Returns the description of the layout area’s horizontal units.
- [func setAccessibilityHorizontalUnitDescription(String?)](nsaccessibilityprotocol/setaccessibilityhorizontalunitdescription(_:).md)
  Sets the description of the layout area’s horizontal units.
- [func accessibilityVerticalUnits() -> NSAccessibilityUnits](nsaccessibilityprotocol/accessibilityverticalunits.md)
  Returns the units that the layout area uses for vertical values.
- [func setAccessibilityVerticalUnits(NSAccessibilityUnits)](nsaccessibilityprotocol/setaccessibilityverticalunits(_:).md)
  Sets the units that the layout area uses for vertical values.
- [func accessibilityVerticalUnitDescription() -> String?](nsaccessibilityprotocol/accessibilityverticalunitdescription.md)
  Returns the description of the layout area’s vertical units.
- [func setAccessibilityVerticalUnitDescription(String?)](nsaccessibilityprotocol/setaccessibilityverticalunitdescription(_:).md)
  Sets the description of the layout area’s vertical units.
- [func accessibilityLayoutPoint(forScreenPoint: NSPoint) -> NSPoint](nsaccessibilityprotocol/accessibilitylayoutpoint(forscreenpoint:).md)
  Converts the provided point in screen coordinates to a point in the layout area’s coordinate system.
- [func accessibilityLayoutSize(forScreenSize: NSSize) -> NSSize](nsaccessibilityprotocol/accessibilitylayoutsize(forscreensize:).md)
  Converts the provided size in screen coordinates to a size in the layout area’s coordinate system.
- [func accessibilityScreenPoint(forLayoutPoint: NSPoint) -> NSPoint](nsaccessibilityprotocol/accessibilityscreenpoint(forlayoutpoint:).md)
  Converts the provided point in the layout area’s coordinates to a point in the screen’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityscreensize(forlayoutsize:))*