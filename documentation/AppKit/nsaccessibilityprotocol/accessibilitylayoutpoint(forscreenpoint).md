# accessibilityLayoutPoint(forScreenPoint:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts the provided point in screen coordinates to a point in the layout area’s coordinate system.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityLayoutPoint(forScreenPoint point: NSPoint) -> NSPoint
```

```objc
- (NSPoint) accessibilityLayoutPointForScreenPoint:(NSPoint) point;
```

## Return Value

A point in the layout area’s coordinate system.

## Parameters

- `point`: A point in the screen’s coordinate system.

## See Also

### Configuring layout
- [func accessibilityHandles() -> [Any]?](./accessibilityhandles%28%29.md)
  Returns the drag handle elements for the layout item element.
- [func setAccessibilityHandles([Any]?)](./setaccessibilityhandles%28_%29.md)
  Sets the drag handle accessibility elements for the layout item element.
- [func accessibilityHorizontalUnits() -> NSAccessibilityUnits](./accessibilityhorizontalunits%28%29.md)
  Returns the units that the layout area uses for horizontal values.
- [func setAccessibilityHorizontalUnits(NSAccessibilityUnits)](./setaccessibilityhorizontalunits%28_%29.md)
  Sets the units that the layout area uses for horizontal values.
- [func accessibilityHorizontalUnitDescription() -> String?](./accessibilityhorizontalunitdescription%28%29.md)
  Returns the description of the layout area’s horizontal units.
- [func setAccessibilityHorizontalUnitDescription(String?)](./setaccessibilityhorizontalunitdescription%28_%29.md)
  Sets the description of the layout area’s horizontal units.
- [func accessibilityVerticalUnits() -> NSAccessibilityUnits](./accessibilityverticalunits%28%29.md)
  Returns the units that the layout area uses for vertical values.
- [func setAccessibilityVerticalUnits(NSAccessibilityUnits)](./setaccessibilityverticalunits%28_%29.md)
  Sets the units that the layout area uses for vertical values.
- [func accessibilityVerticalUnitDescription() -> String?](./accessibilityverticalunitdescription%28%29.md)
  Returns the description of the layout area’s vertical units.
- [func setAccessibilityVerticalUnitDescription(String?)](./setaccessibilityverticalunitdescription%28_%29.md)
  Sets the description of the layout area’s vertical units.
- [func accessibilityLayoutSize(forScreenSize: NSSize) -> NSSize](./accessibilitylayoutsize%28forscreensize%29.md)
  Converts the provided size in screen coordinates to a size in the layout area’s coordinate system.
- [func accessibilityScreenPoint(forLayoutPoint: NSPoint) -> NSPoint](./accessibilityscreenpoint%28forlayoutpoint%29.md)
  Converts the provided point in the layout area’s coordinates to a point in the screen’s coordinate system.
- [func accessibilityScreenSize(forLayoutSize: NSSize) -> NSSize](./accessibilityscreensize%28forlayoutsize%29.md)
  Converts the provided size in the layout area’s coordinates to a size in the screen’s coordinate system.
- [accessibilityHandles](../nsaccessibility-c.protocol/accessibilityhandles.md)
  The drag handle accessibility elements for the layout item element.
- [accessibilityHorizontalUnits](../nsaccessibility-c.protocol/accessibilityhorizontalunits.md)
  The units that the layout area uses for horizontal values.
- [accessibilityHorizontalUnitDescription](../nsaccessibility-c.protocol/accessibilityhorizontalunitdescription.md)
  A description of the layout area’s horizontal units.
- [accessibilityVerticalUnits](../nsaccessibility-c.protocol/accessibilityverticalunits.md)
  The units that the layout area uses for vertical values.
- [accessibilityVerticalUnitDescription](../nsaccessibility-c.protocol/accessibilityverticalunitdescription.md)
  A description of the layout area’s vertical units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilitylayoutpoint(forscreenpoint:))*