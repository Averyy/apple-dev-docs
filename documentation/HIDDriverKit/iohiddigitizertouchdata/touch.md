# touch

**Framework**: HIDDriverKit  
**Kind**: property

A single-bit Boolean that indicates whether the finger is in contact with the surface of the digitizer.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
uint32_t touch;
```

## See Also

- [identifier](iohiddigitizertouchdata/identifier.md)
  A unique contact identifier.
- [x](iohiddigitizertouchdata/x.md)
  An x-coordinate value in the range `0.0` to `1.0`.
- [y](iohiddigitizertouchdata/y.md)
  A y-coordinate value in the range `0.0` to `1.0`.
- [inRange](iohiddigitizertouchdata/inrange.md)
  A single-bit Boolean that indicates whether the finger is in range.
- [touchValid](iohiddigitizertouchdata/touchvalid.md)
  A single-bit Boolean that indicates whether the touch contact was intended.
- [touchChanged](iohiddigitizertouchdata/touchchanged.md)
  A single-bit Boolean that indicates whether the touch variable changed since the last event was dispatched.
- [positionChanged](iohiddigitizertouchdata/positionchanged.md)
  A single-bit Boolean that indicates whether the x or y position changed since the last event was dispatched.
- [rangeChanged](iohiddigitizertouchdata/rangechanged.md)
  A single-bit Boolean that indicates whether the range variable changed since the last event was dispatched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizertouchdata/touch)*