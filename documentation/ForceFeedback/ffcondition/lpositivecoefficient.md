# lPositiveCoefficient

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

Coefficient constant on the positive side of the offset, in the range from -10,000 through 10,000.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var lPositiveCoefficient: LONG
```

```c
LONG lPositiveCoefficient;
```

## See Also

### Instance Properties
- [var dwNegativeSaturation: DWORD](./dwnegativesaturation.md)
  Maximum force output on the negative side of the offset, in the range from 0 through 10,000.
- [var dwPositiveSaturation: DWORD](./dwpositivesaturation.md)
  Maximum force output on the positive side of the offset, in the range from 0 through 10,000.
- [var lDeadBand: LONG](./ldeadband.md)
  Region around **lOffset** in which the condition is not active, in the range from 0 through 10,000. In other words, the condition is not active between **lOffset** minus **lDeadBand** and **lOffset** plus **lDeadBand**.
- [var lNegativeCoefficient: LONG](./lnegativecoefficient.md)
  Coefficient constant on the negative side of the offset, in the range from -10,000 through 10,000.
- [var lOffset: LONG](./loffset.md)
  Offset for the condition, in the range from -10,000 through 10,000.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcondition/lpositivecoefficient)*