# rotation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rotation in degrees of the tablet pointing device associated with this event.

**Availability**:
- macOS

## Declaration

```swift
var rotation: Float { get }
```

```objc
@property (readonly) float rotation;
```

## Discussion

Many devices do not support rotation, in which case the returned value is 0.0. This property is valid only for mouse events with subtype `NSTabletPointEventSubtype` and for `NSTabletPoint` events.

## See Also

### Related Documentation
- [var pressure: Float](./pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
### Getting tablet pointing information
- [var absoluteX: Int](./absolutex.md)
  The absolute x coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteY: Int](./absolutey.md)
  The absolute y coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteZ: Int](./absolutez.md)
  The absolute z coordinate of pointing device on its tablet at full tablet resolution.
- [var buttonMask: NSEvent.ButtonMask](./buttonmask-swift.property.md)
  A bit mask identifying the buttons pressed for a tablet event.
- [NSEvent.ButtonMask](./buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [var tangentialPressure: Float](./tangentialpressure.md)
  The tangential pressure on the device that generated this event.
- [var tilt: NSPoint](./tilt.md)
  The scaled tilt values of the pointing device that generated this event.
- [var vendorDefined: Any](./vendordefined.md)
  An array of three vendor-defined number objects associated with a pointing-type event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/rotation)*