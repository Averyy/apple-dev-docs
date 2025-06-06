# IOHIDDigitizerTouchData

**Framework**: HIDDriverKit  
**Kind**: struct

A structure containing the current digitizer touch data.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef struct IOHIDDigitizerTouchData { ... } IOHIDDigitizerTouchData;
```

#### Overview

Pass this structure to the [`dispatchDigitizerTouchEvent`](iohideventservice/dispatchdigitizertouchevent.md) method when dispatching touch events.

## Topics

### Getting the Touch Data
- [identifier](iohiddigitizertouchdata/identifier.md)
  A unique contact identifier.
- [x](iohiddigitizertouchdata/x.md)
  An x-coordinate value in the range `0.0` to `1.0`.
- [y](iohiddigitizertouchdata/y.md)
  A y-coordinate value in the range `0.0` to `1.0`.
- [inRange](iohiddigitizertouchdata/inrange.md)
  A single-bit Boolean that indicates whether the finger is in range.
- [touch](iohiddigitizertouchdata/touch.md)
  A single-bit Boolean that indicates whether the finger is in contact with the surface of the digitizer.
- [touchValid](iohiddigitizertouchdata/touchvalid.md)
  A single-bit Boolean that indicates whether the touch contact was intended.
- [touchChanged](iohiddigitizertouchdata/touchchanged.md)
  A single-bit Boolean that indicates whether the touch variable changed since the last event was dispatched.
- [positionChanged](iohiddigitizertouchdata/positionchanged.md)
  A single-bit Boolean that indicates whether the x or y position changed since the last event was dispatched.
- [rangeChanged](iohiddigitizertouchdata/rangechanged.md)
  A single-bit Boolean that indicates whether the range variable changed since the last event was dispatched.

## See Also

- [IOHIDDigitizerStylusData](iohiddigitizerstylusdata.md)
  A structure containing digitizer stylus data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizertouchdata)*