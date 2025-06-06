# IOHIDDigitizerStylusData

**Framework**: HIDDriverKit  
**Kind**: struct

A structure containing digitizer stylus data.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef struct IOHIDDigitizerStylusData { ... } IOHIDDigitizerStylusData;
```

#### Overview

When dispatching stylus events, allocate an `IOHIDDigitizerStylusData` structure, fill it with stylus data, and pass it to the [`dispatchDigitizerStylusEvent`](iohideventservice/dispatchdigitizerstylusevent.md) method.

## Topics

### Getting the Stylus Data
- [identifier](iohiddigitizerstylusdata/identifier.md)
  A unique stylus identifier.
- [x](iohiddigitizerstylusdata/x.md)
  An x-axis value in the range `0.0` to `1.0`.
- [y](iohiddigitizerstylusdata/y.md)
  A y-axis value in the range `0.0` to `1.0`.
- [tipPressure](iohiddigitizerstylusdata/tippressure.md)
  A tip pressure value in the range `0.0` to `1.0`.
- [barrelPressure](iohiddigitizerstylusdata/barrelpressure.md)
  The barrel pressure value in the range `0.0` to `1.0`.
- [tiltX](iohiddigitizerstylusdata/tiltx.md)
  The tilt of the stylus across the x-axis.
- [tiltY](iohiddigitizerstylusdata/tilty.md)
  The tilt of the stylus across the y-axis.
- [twist](iohiddigitizerstylusdata/twist.md)
  The clockwise rotation of the stylus.
- [pointerType](iohiddigitizerstylusdata/pointertype.md)
  An optional pointer type defined by vendor.
- [effect](iohiddigitizerstylusdata/effect.md)
  An optional stylus effect defined by vendor.
- [uniqueID](iohiddigitizerstylusdata/uniqueid.md)
  An optional unique identifier for the stylus.
- [inRange](iohiddigitizerstylusdata/inrange.md)
  A single-bit Boolean that indicates whether the stylus is in range.
- [tip](iohiddigitizerstylusdata/tip.md)
  A single-bit Boolean that indicates whether the tip of the stylus is in contact with the surface of the digitizer.
- [barrelSwitch](iohiddigitizerstylusdata/barrelswitch.md)
  A single-bit Boolean that indicates whether the barrel switch button is pressed.
- [invert](iohiddigitizerstylusdata/invert.md)
  A single-bit Boolean that indicates whether the stylus is inverted.
- [eraser](iohiddigitizerstylusdata/eraser.md)
  A Boolean value that indicates whether the inverted stylus is in contact with the surface of the digitizer.
- [tipChanged](iohiddigitizerstylusdata/tipchanged.md)
  A single-bit Boolean that indicates whether the tip contact status changed since the last event was dispatched.
- [positionChanged](iohiddigitizerstylusdata/positionchanged.md)
  A single-bit Boolean that indicates whether the x or y position changed since the last event was dispatched.
- [rangeChanged](iohiddigitizerstylusdata/rangechanged.md)
  A single-bit Boolean that indicates whether the in-range status changed since the last event was dispatched.

## See Also

- [IOHIDDigitizerTouchData](iohiddigitizertouchdata.md)
  A structure containing the current digitizer touch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizerstylusdata)*