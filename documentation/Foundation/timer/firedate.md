# fireDate

**Framework**: Foundation  
**Kind**: property

The date at which the timer will fire.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fireDate: Date { get set }
```

#### Discussion

If the timer is no longer valid, the last date at which the timer fired.

You can set this property to adjust the firing time of a repeating timer. Although resetting a timer’s next firing time is a relatively expensive operation, it may be more efficient in some situations. For example, you could use it in situations where you want to repeat an action multiple times in the future, but at irregular time intervals. Adjusting the firing time of a single timer would likely incur less expense than creating multiple timer objects, scheduling each one on a run loop, and then destroying them.

You should not change the fire date of a timer that has been invalidated, which includes non-repeating timers that have already fired. You could potentially change the fire date of a non-repeating timer that had not yet fired, although you should always do so from the thread to which the timer is attached to avoid potential race conditions.

Use the [`isValid`](timer/isvalid.md) method to verify that the timer is valid.

## See Also

- [var isValid: Bool](timer/isvalid.md)
  A Boolean value that indicates whether the timer is currently valid.
- [var timeInterval: TimeInterval](timer/timeinterval.md)
  The timer’s time interval, in seconds.
- [var userInfo: Any?](timer/userinfo.md)
  The receiver’s `userInfo` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/firedate)*