# accessibilityVerticalUnits

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The units that the layout area uses for vertical values.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property NSAccessibilityUnits accessibilityVerticalUnits;
```

#### Discussion

For a list of possible values, see [`NSAccessibilityUnits`](../nsaccessibilityunits.md).

## See Also

### Configuring layout
- [func accessibilityLayoutPoint(forScreenPoint: NSPoint) -> NSPoint](../nsaccessibilityprotocol/accessibilitylayoutpoint%28forscreenpoint%29.md)
  Converts the provided point in screen coordinates to a point in the layout area’s coordinate system.
- [func accessibilityLayoutSize(forScreenSize: NSSize) -> NSSize](../nsaccessibilityprotocol/accessibilitylayoutsize%28forscreensize%29.md)
  Converts the provided size in screen coordinates to a size in the layout area’s coordinate system.
- [func accessibilityScreenPoint(forLayoutPoint: NSPoint) -> NSPoint](../nsaccessibilityprotocol/accessibilityscreenpoint%28forlayoutpoint%29.md)
  Converts the provided point in the layout area’s coordinates to a point in the screen’s coordinate system.
- [func accessibilityScreenSize(forLayoutSize: NSSize) -> NSSize](../nsaccessibilityprotocol/accessibilityscreensize%28forlayoutsize%29.md)
  Converts the provided size in the layout area’s coordinates to a size in the screen’s coordinate system.
- [accessibilityHandles](./accessibilityhandles.md)
  The drag handle accessibility elements for the layout item element.
- [accessibilityHorizontalUnits](./accessibilityhorizontalunits.md)
  The units that the layout area uses for horizontal values.
- [accessibilityHorizontalUnitDescription](./accessibilityhorizontalunitdescription.md)
  A description of the layout area’s horizontal units.
- [accessibilityVerticalUnitDescription](./accessibilityverticalunitdescription.md)
  A description of the layout area’s vertical units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityverticalunits)*