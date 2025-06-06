# vendorDefined

**Framework**: AppKit  
**Kind**: property

An array of three vendor-defined number objects associated with a pointing-type event.

**Availability**:
- macOS ?+

## Declaration

```swift
var vendorDefined: Any { get }
```

#### Discussion

This property contains an array of three [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects. Each object encapsulates a `short` value that vendors may return for various reasons; see the vendor documentation for details.This method is valid for mouse events with subtype [`NSTabletPointEventSubtype`](nstabletpointeventsubtype.md) and for [`NSTabletPoint`](nstabletpoint.md) events.

## See Also

- [var absoluteX: Int](nsevent/absolutex.md)
  The absolute x coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteY: Int](nsevent/absolutey.md)
  The absolute y coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteZ: Int](nsevent/absolutez.md)
  The absolute z coordinate of pointing device on its tablet at full tablet resolution.
- [var buttonMask: NSEvent.ButtonMask](nsevent/buttonmask-swift.property.md)
  A bit mask identifying the buttons pressed for a tablet event.
- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [var rotation: Float](nsevent/rotation.md)
  The rotation in degrees of the tablet pointing device associated with this event.
- [var tangentialPressure: Float](nsevent/tangentialpressure.md)
  The tangential pressure on the device that generated this event.
- [var tilt: NSPoint](nsevent/tilt.md)
  The scaled tilt values of the pointing device that generated this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/vendordefined)*