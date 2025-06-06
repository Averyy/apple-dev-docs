# CMTime

**Framework**: Core Media  
**Kind**: struct

A structure that represents time.

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
struct CMTime
```

#### Overview

Core Media represents time as a rational value, with a time value as the numerator and timescale as the denominator. The structure can represent a specific numeric time in the media timeline, and can also represent nonnumeric values like invalid and indefinite times or positive and negative infinity.

## Topics

### Creating a Time
- [init(value: CMTimeValue, timescale: CMTimeScale)](cmtime/init(value:timescale:).md)
  Creates a time with a value and timescale.
- [init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)](cmtime/init(value:timescale:flags:epoch:).md)
  Creates a time with a value, timescale, flags, and epoch.
- [init(seconds: Double, preferredTimescale: CMTimeScale)](cmtime/init(seconds:preferredtimescale:).md)
  Creates a time that represents number of seconds in a preferred timescale.
- [init()](cmtime/init.md)
  Creates a time with an invalid value.
### Inspecting a Time
- [var seconds: Double](cmtime/seconds.md)
  A representation of the time in seconds.
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
### Performing Time Calcualtions
- [static func + (CMTime, CMTime) -> CMTime](cmtime/+(_:_:).md)
  Returns a new time that represents the sum of two times.
- [static func - (CMTime, CMTime) -> CMTime](cmtime/-(_:_:).md)
  Returns a new time that represents the difference between two times.
### Changing the Timescale
- [func convertScale(Int32, method: CMTimeRoundingMethod) -> CMTime](cmtime/convertscale(_:method:).md)
  Converts the source time to a new timescale using the specified rounding method.
- [enum CMTimeRoundingMethod](cmtimeroundingmethod.md)
  An enumeration of rounding methods to use when performing time calculations.
### Accessing Time Values
- [var value: CMTimeValue](cmtime/value.md)
  A time value that represents the numerator of a rational time.
- [var timescale: CMTimeScale](cmtime/timescale.md)
  A timescale that represents the denominator of a rational time.
- [var flags: CMTimeFlags](cmtime/flags.md)
  The flags associated with a time.
- [var epoch: CMTimeEpoch](cmtime/epoch.md)
  The epoch of the time.
### Constants
- [static let zero: CMTime](cmtime/zero.md)
  A value that represents time zero.
- [static let invalid: CMTime](cmtime/invalid.md)
  A value that represents an invalid time.
- [static let indefinite: CMTime](cmtime/indefinite.md)
  A value that represents an indefinite time.
- [static let negativeInfinity: CMTime](cmtime/negativeinfinity.md)
  A value that represents negative infinity.
- [static let positiveInfinity: CMTime](cmtime/positiveinfinity.md)
  A value that represents positive infinity.
### Operators
- [static func != (CMTime, CMTime) -> Bool](cmtime/!=(_:_:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CMTimeValue](cmtimevalue.md)
  An integer time value.
- [typealias CMTimeScale](cmtimescale.md)
  An integer timescale.
- [typealias CMTimeEpoch](cmtimeepoch.md)
  An epoch for a time.
- [struct CMTimeFlags](cmtimeflags.md)
  A structure that defines the flags for a time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime)*