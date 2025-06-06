# setTimerNextFireTime(_:fireTime:)

**Framework**: Core Media  
**Kind**: method

Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func setTimerNextFireTime<T>(_ timer: T, fireTime: CMTime) throws where T : DispatchSourceTimer
```

## See Also

- [func setTimerNextFireTime(Timer, fireTime: CMTime) throws](cmtimebase/settimernextfiretime(_:firetime:)-13hjt.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func setTimerToFireImmediately(Timer) throws](cmtimebase/settimertofireimmediately(_:)-9t3wi.md)
  Sets the timer to fire immediately once, overriding any previous calls.
- [func setTimerToFireImmediately<T>(T) throws](cmtimebase/settimertofireimmediately(_:)-4903g.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/settimernextfiretime(_:firetime:)-2yvaa)*