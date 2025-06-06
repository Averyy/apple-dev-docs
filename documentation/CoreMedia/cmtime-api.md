# CMTime APIs

**Framework**: Core Media

A structure that represents time.

#### Overview

Core Media represents time as a rational value, with a time value as the numerator and timescale as the denominator. The structure can represent a specific numeric time in the media timeline, and can also represent nonnumeric values like invalid and indefinite times or positive and negative infinity.

## Topics

### Creating a Time
- [func CMTimeMake(value: Int64, timescale: Int32) -> CMTime](cmtimemake(value:timescale:).md)
  Creates a time with a value and timescale.
- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](cmtimemakewithepoch(value:timescale:epoch:).md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeWithSeconds(Float64, preferredTimescale: Int32) -> CMTime](cmtimemakewithseconds(_:preferredtimescale:).md)
  Creates a time that represents a number of seconds in a preferred timescale.
- [func CMTimeMakeFromDictionary(CFDictionary?) -> CMTime](cmtimemakefromdictionary(_:).md)
  Creates a time from a dictionary representation of its fields.
### Inspecting a Time
- [func CMTimeGetSeconds(CMTime) -> Float64](cmtimegetseconds(_:).md)
  Returns a representation of the time in seconds.
- [func CMTimeAbsoluteValue(CMTime) -> CMTime](cmtimeabsolutevalue(_:).md)
  Returns the absolute value of a time.
- [func CMTIME_IS_VALID(CMTime) -> Bool](cmtime_is_valid(_:).md)
  Returns a Boolean value that indicates whether a given time is valid.
- [func CMTIME_IS_INVALID(CMTime) -> Bool](cmtime_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a given time is invalid.
- [func CMTIME_IS_POSITIVEINFINITY(CMTime) -> Bool](cmtime_is_positiveinfinity(_:).md)
  Returns a Boolean value that indicates whether a given time is positive infinity.
- [func CMTIME_IS_NEGATIVEINFINITY(CMTime) -> Bool](cmtime_is_negativeinfinity(_:).md)
  Returns a Boolean value that indicates whether a given time is negative infinity.
- [func CMTIME_IS_INDEFINITE(CMTime) -> Bool](cmtime_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a given time is indefinite.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](cmtime_is_numeric(_:).md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](cmtime_has_been_rounded(_:).md)
  Returns a Boolean value that indicates whether the system rounded the time value.
### Performing Time Calculations
- [func CMTimeAdd(CMTime, CMTime) -> CMTime](cmtimeadd(_:_:).md)
  Returns the sum of two times.
- [func CMTimeSubtract(CMTime, CMTime) -> CMTime](cmtimesubtract(_:_:).md)
  Returns the difference between two times.
- [func CMTimeMultiply(CMTime, multiplier: Int32) -> CMTime](cmtimemultiply(_:multiplier:).md)
  Returns the result of multiplying a time by an integer multiplier.
- [func CMTimeMultiplyByFloat64(CMTime, multiplier: Float64) -> CMTime](cmtimemultiplybyfloat64(_:multiplier:).md)
  Returns the result of multiplying a time by a floating-point multiplier.
- [func CMTimeMultiplyByRatio(CMTime, multiplier: Int32, divisor: Int32) -> CMTime](cmtimemultiplybyratio(_:multiplier:divisor:).md)
  Returns the result of multiplying a time by an integer multiplier, and then dividing the result by the divisor.
### Changing the Timescale
- [func CMTimeConvertScale(CMTime, timescale: Int32, method: CMTimeRoundingMethod) -> CMTime](cmtimeconvertscale(_:timescale:method:).md)
  Converts the source time to a new timescale using the specified rounding method.
- [enum CMTimeRoundingMethod](cmtimeroundingmethod.md)
  An enumeration of rounding methods to use when performing time calculations.
### Comparing Times
- [func CMTimeCompare(CMTime, CMTime) -> Int32](cmtimecompare(_:_:).md)
  Returns the numerical relationship of two times.
- [func CMTimeMaximum(CMTime, CMTime) -> CMTime](cmtimemaximum(_:_:).md)
  Returns the greater of two time values.
- [func CMTimeMinimum(CMTime, CMTime) -> CMTime](cmtimeminimum(_:_:).md)
  Returns the lesser of two time values.
### Representing Times
- [func CMTimeShow(CMTime)](cmtimeshow(_:).md)
  Prints a description of the time to the console.
- [func CMTimeCopyDescription(allocator: CFAllocator?, time: CMTime) -> CFString?](cmtimecopydescription(allocator:time:).md)
  Creates a string representation of the time.
- [func CMTimeCopyAsDictionary(CMTime, allocator: CFAllocator?) -> CFDictionary?](cmtimecopyasdictionary(_:allocator:).md)
  Creates a dictionary representation of the time.
### Data Types
- [struct CMTime](cmtime.md)
  A structure that represents time.
- [typealias CMTimeValue](cmtimevalue.md)
  An integer time value.
- [typealias CMTimeScale](cmtimescale.md)
  An integer timescale.
- [typealias CMTimeEpoch](cmtimeepoch.md)
  An epoch for a time.
- [struct CMTimeFlags](cmtimeflags.md)
  A structure that defines the flags for a time value.
### Constants
- [Time](cmtime-time.md)
  Defined time values.
- [Timescale](cmtime-timescale.md)
  Defined timescale values.
- [Dictionary Keys](cmtime-dictionary-keys.md)
  Keys to use when working with dictionary representations of time.

## See Also

- [CMTimeRange APIs](cmtimerange-api.md)
  A structure that represents a range of time.
- [CMTimeMapping APIs](cmtimemapping-api.md)
  A structure that maps a segment of a source time range to a target time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime-api)*