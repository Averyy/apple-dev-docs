# NSRulerView

**Framework**: AppKit  
**Kind**: class

A ruler and the markers above or to the side of a scroll view’s document view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSRulerView
```

#### Overview

Views within the scroll view can become clients of the ruler view, having it display markers for their elements, and receiving messages from the ruler view when the user manipulates the markers.

##### Principal Attributes

- Displays markers that represent elements of the client view.
- Displays in arbitrary units.
- Provides for an accessory view containing extra controls.

##### Creation

- [`hasHorizontalRuler`](nsscrollview/hashorizontalruler.md) (`NSScrollView`)
- [`hasVerticalRuler`](nsscrollview/hasverticalruler.md) (`NSScrollView`)
- [`init(scrollView:orientation:)`](nsrulerview/init(scrollview:orientation:).md) Designated initializer.

##### Commonly Used Methods

##### Overview

See NSRulerMarkerClientViewDelegation for delegate methods that may be of interest.

## Topics

### Creating a Ruler View
- [init(scrollView: NSScrollView?, orientation: NSRulerView.Orientation)](nsrulerview/init(scrollview:orientation:).md)
  Initializes a newly allocated NSRulerView to have `orientation` (`NSHorizontalRuler` or `NSVerticalRuler`) within `aScrollView`.
- [init(coder: NSCoder)](nsrulerview/init(coder:).md)
### Altering measurement units
- [class func registerUnit(withName: NSRulerView.UnitName, abbreviation: String, unitToPointsConversionFactor: CGFloat, stepUpCycle: [NSNumber], stepDownCycle: [NSNumber])](nsrulerview/registerunit(withname:abbreviation:unittopointsconversionfactor:stepupcycle:stepdowncycle:).md)
  Registers a new unit of measurement with the NSRulerView class, making it available to all instances of NSRulerView.
- [var measurementUnits: NSRulerView.UnitName](nsrulerview/measurementunits.md)
  The measurement units used by the ruler to `unitName`.
- [NSRulerView.UnitName](nsrulerview/unitname.md)
### Setting the client view
- [var clientView: NSView?](nsrulerview/clientview.md)
  The receiver’s client view, if it has one.
### Setting an accessory view
- [var accessoryView: NSView?](nsrulerview/accessoryview.md)
  The receiver’s accessory view to `aView`.
### Setting the zero mark position
- [var originOffset: CGFloat](nsrulerview/originoffset.md)
  The distance to the zero hash mark from the bounds origin of the NSScrollView’s document view (not of the receiver’s client view), in the document view’s coordinate system.
### Adding and removing markers
- [var markers: [NSRulerMarker]?](nsrulerview/markers.md)
  The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.
- [func addMarker(NSRulerMarker)](nsrulerview/addmarker(_:).md)
  Adds `aMarker` to the receiver, without consulting the client view for approval.
- [func removeMarker(NSRulerMarker)](nsrulerview/removemarker(_:).md)
  Removes `aMarker` from the receiver, without consulting the client view for approval.
- [func trackMarker(NSRulerMarker, withMouseEvent: NSEvent) -> Bool](nsrulerview/trackmarker(_:withmouseevent:).md)
  Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.
### Drawing temporary ruler lines
- [func moveRulerline(fromLocation: CGFloat, toLocation: CGFloat)](nsrulerview/moverulerline(fromlocation:tolocation:).md)
  Draws temporary lines in the ruler area.
### Drawing
- [func drawHashMarksAndLabels(in: NSRect)](nsrulerview/drawhashmarksandlabels(in:).md)
  Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.
- [func drawMarkers(in: NSRect)](nsrulerview/drawmarkers(in:).md)
  Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.
- [func invalidateHashMarks()](nsrulerview/invalidatehashmarks.md)
  Forces recalculation of the hash mark spacing for the next time the receiver is displayed.
### Ruler layout
- [var scrollView: NSScrollView?](nsrulerview/scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](nsrulerview/orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](nsrulerview/orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](nsrulerview/orientation-swift.property.md).
- [var reservedThicknessForAccessoryView: CGFloat](nsrulerview/reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](nsrulerview/reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](nsrulerview/rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](nsrulerview/requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](nsrulerview/baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSRulerMarker](nsrulermarker.md)
  A symbol on a ruler view, indicating a location for the graphics element it represents in the client of the ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview)*