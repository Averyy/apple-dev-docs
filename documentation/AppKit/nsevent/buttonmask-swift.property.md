# buttonMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A bit mask identifying the buttons pressed for a tablet event.

**Availability**:
- macOS

## Declaration

```swift
var buttonMask: NSEvent.ButtonMask { get }
```

```objc
@property (readonly) NSEventButtonMask buttonMask;
```

#### Discussion

Use one or more of the button-mask constants described in `Getting Unicode Values` to determine which of the pointing device’s buttons are pressed. This property is valid only for mouse events with a subtype of `NSTabletPointEventSubtype` and for events of type `NSTabletPoint`; otherwise, the property is set to `0`.

## See Also

### Getting tablet pointing information
- [var absoluteX: Int](./absolutex.md)
  The absolute x coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteY: Int](./absolutey.md)
  The absolute y coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteZ: Int](./absolutez.md)
  The absolute z coordinate of pointing device on its tablet at full tablet resolution.
- [NSEvent.ButtonMask](./buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [var rotation: Float](./rotation.md)
  The rotation in degrees of the tablet pointing device associated with this event.
- [var tangentialPressure: Float](./tangentialpressure.md)
  The tangential pressure on the device that generated this event.
- [var tilt: NSPoint](./tilt.md)
  The scaled tilt values of the pointing device that generated this event.
- [var vendorDefined: Any](./vendordefined.md)
  An array of three vendor-defined number objects associated with a pointing-type event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/buttonmask-swift.property)*