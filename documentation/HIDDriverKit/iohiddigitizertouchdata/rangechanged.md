# rangeChanged

**Framework**: HIDDriverKit  
**Kind**: property

A single-bit Boolean that indicates whether the range variable changed since the last event was dispatched.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
uint32_t rangeChanged;
```

#### Discussion

For example, this property is `1` if the value in the [`inRange`](iohiddigitizertouchdata/inrange.md) field changed from `0` to `1` since the last event.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizertouchdata/rangechanged)*