# addTimer(_:on:)

**Framework**: Core Media  
**Kind**: method

Adds the timer to the list of timers the timebase manages.

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
func addTimer(_ timer: Timer, on runloop: RunLoop) throws
```

## See Also

- [func addTimer<T>(T) throws](cmtimebase/addtimer(_:).md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func removeTimer(Timer) throws](cmtimebase/removetimer(_:)-4f6re.md)
  Removes the timer from the list of timers the timebase manages.
- [func removeTimer<T>(T) throws](cmtimebase/removetimer(_:)-448o2.md)
  Removes the timer dispatch source from the list of timers the timebase manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/addtimer(_:on:))*