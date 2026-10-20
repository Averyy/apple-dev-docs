# barrelSwitch

**Framework**: HIDDriverKit  
**Kind**: property  
**Role**: Instance Property

A single-bit Boolean that indicates whether the barrel switch button is pressed.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
uint32_t barrelSwitch;
```

## See Also

### Getting the Stylus Data
- [identifier](./identifier.md)
  A unique stylus identifier.
- [x](./x.md)
  An x-axis value in the range `0.0` to `1.0`.
- [y](./y.md)
  A y-axis value in the range `0.0` to `1.0`.
- [tipPressure](./tippressure.md)
  A tip pressure value in the range `0.0` to `1.0`.
- [barrelPressure](./barrelpressure.md)
  The barrel pressure value in the range `0.0` to `1.0`.
- [tiltX](./tiltx.md)
  The tilt of the stylus across the x-axis.
- [tiltY](./tilty.md)
  The tilt of the stylus across the y-axis.
- [twist](./twist.md)
  The clockwise rotation of the stylus.
- [pointerType](./pointertype.md)
  An optional pointer type defined by vendor.
- [effect](./effect.md)
  An optional stylus effect defined by vendor.
- [uniqueID](./uniqueid.md)
  An optional unique identifier for the stylus.
- [inRange](./inrange.md)
  A single-bit Boolean that indicates whether the stylus is in range.
- [tip](./tip.md)
  A single-bit Boolean that indicates whether the tip of the stylus is in contact with the surface of the digitizer.
- [invert](./invert.md)
  A single-bit Boolean that indicates whether the stylus is inverted.
- [eraser](./eraser.md)
  A Boolean value that indicates whether the inverted stylus is in contact with the surface of the digitizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizerstylusdata/barrelswitch)*