# setTimerToFireImmediately(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Sets the timer to fire immediately once, overriding any previous calls.

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
func setTimerToFireImmediately(_ timer: Timer) throws
```

## See Also

### Setting Timers
- [func setTimerNextFireTime(Timer, fireTime: CMTime) throws](./settimernextfiretime%28_,firetime%29-13hjt.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func setTimerNextFireTime<T>(T, fireTime: CMTime) throws](./settimernextfiretime%28_,firetime%29-2yvaa.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func setTimerToFireImmediately<T>(T) throws](./settimertofireimmediately%28_%29-4903g.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/settimertofireimmediately(_:)-9t3wi)*