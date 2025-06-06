# negate()

**Framework**: Combine  
**Kind**: method

Replaces this value with its additive inverse.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func negate()
```

#### Discussion

The following example uses the `negate()` method to negate the value of an integer `x`:

```swift
var x = 21
x.negate()
// x == -21
```

The resulting value must be representable within the value’s type. In particular, negating a signed, fixed-width integer type’s minimum results in a value that cannot be represented.

```swift
var y = Int8.min
y.negate()
// Overflow error
```

## See Also

- [static func * (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func *= (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func + (Self) -> Self](immediatescheduler/schedulertimetype/stride/+(_:).md)
  Returns the given number unchanged.
- [static func + (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/+(_:_:).md)
  Adds two values and produces their sum.
- [static func += (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func - (Self) -> Self](immediatescheduler/schedulertimetype/stride/-(_:).md)
  Returns the additive inverse of the specified value.
- [static func - (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func -= (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride/negate())*