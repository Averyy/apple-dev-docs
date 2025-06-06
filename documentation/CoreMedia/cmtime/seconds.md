# seconds

**Framework**: Core Media  
**Kind**: property

A representation of the time in seconds.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst ?+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var seconds: Double { get }
```

#### Discussion

If the time is [`invalid`](cmsampletiminginfo/invalid.md) or [`indefinite`](cmtimeflags/indefinite.md), the value equals [`nan`](https://developer.apple.com/documentation/Swift/Double/nan).

## See Also

- [var hasBeenRounded: Bool](cmtime/hasbeenrounded.md)
  A Boolean value that indicates whether the system rounded the time.
- [var isValid: Bool](cmtime/isvalid.md)
  A Boolean value that indicates whether a time is valid.
- [var isNumeric: Bool](cmtime/isnumeric.md)
  A Boolean value that indicates whether a time is numeric.
- [var isIndefinite: Bool](cmtime/isindefinite.md)
  A Boolean value that indicates whether a time is indefinite.
- [var isPositiveInfinity: Bool](cmtime/ispositiveinfinity.md)
  A Boolean value that indicates whether a time represents positive infinity.
- [var isNegativeInfinity: Bool](cmtime/isnegativeinfinity.md)
  A Boolean value that indicates whether a time represents negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/seconds)*