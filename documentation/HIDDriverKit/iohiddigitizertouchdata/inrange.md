# inRange

**Framework**: HIDDriverKit  
**Kind**: property  
**Role**: Instance Property

A single-bit Boolean that indicates whether the finger is in range.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
uint32_t inRange;
```

## See Also

### Getting the Touch Data
- [identifier](./identifier.md)
  A unique contact identifier.
- [x](./x.md)
  An x-coordinate value in the range `0.0` to `1.0`.
- [y](./y.md)
  A y-coordinate value in the range `0.0` to `1.0`.
- [touch](./touch.md)
  A single-bit Boolean that indicates whether the finger is in contact with the surface of the digitizer.
- [touchValid](./touchvalid.md)
  A single-bit Boolean that indicates whether the touch contact was intended.
- [touchChanged](./touchchanged.md)
  A single-bit Boolean that indicates whether the touch variable changed since the last event was dispatched.
- [positionChanged](./positionchanged.md)
  A single-bit Boolean that indicates whether the x or y position changed since the last event was dispatched.
- [rangeChanged](./rangechanged.md)
  A single-bit Boolean that indicates whether the range variable changed since the last event was dispatched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizertouchdata/inrange)*