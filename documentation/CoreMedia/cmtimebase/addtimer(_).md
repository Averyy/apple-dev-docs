# addTimer(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Adds the timer dispatch source to the list of timers the timebase manages.

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
func addTimer<T>(_ timer: T) throws where T : DispatchSourceTimer
```

## See Also

### Adding and Removing Timers
- [func addTimer(Timer, on: RunLoop) throws](./addtimer%28_,on%29.md)
  Adds the timer to the list of timers the timebase manages.
- [func removeTimer(Timer) throws](./removetimer%28_%29-4f6re.md)
  Removes the timer from the list of timers the timebase manages.
- [func removeTimer<T>(T) throws](./removetimer%28_%29-448o2.md)
  Removes the timer dispatch source from the list of timers the timebase manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/addtimer(_:))*