# CMTimeFlags

**Framework**: Core Media  
**Kind**: struct

A structure that defines the flags for a time value.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CMTimeFlags
```

## Topics

### Properties
- [static var valid: CMTimeFlags](cmtimeflags/valid.md)
  A flag that indicates a time is valid.
- [static var hasBeenRounded: CMTimeFlags](cmtimeflags/hasbeenrounded.md)
  A flag that indicates a previous time calculation rounded the result.
- [static var positiveInfinity: CMTimeFlags](cmtimeflags/positiveinfinity.md)
  A flag that indicates the time is positive infinity.
- [static var negativeInfinity: CMTimeFlags](cmtimeflags/negativeinfinity.md)
  A flag that indicates the time is negative infinity.
- [static var indefinite: CMTimeFlags](cmtimeflags/indefinite.md)
  A flag that indicates the time is indefinite.
- [static var impliedValueFlagsMask: CMTimeFlags](cmtimeflags/impliedvalueflagsmask.md)
  A flag that indicates the time is positive or negative infinity, or indefinite.
### Initializers
- [init(rawValue: UInt32)](cmtimeflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CMTime](cmtime.md)
  A structure that represents time.
- [typealias CMTimeValue](cmtimevalue.md)
  An integer time value.
- [typealias CMTimeScale](cmtimescale.md)
  An integer timescale.
- [typealias CMTimeEpoch](cmtimeepoch.md)
  An epoch for a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeflags)*