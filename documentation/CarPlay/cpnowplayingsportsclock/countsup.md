# countsUp

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the event clock counts up.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var countsUp: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL countsUp;
```

## Discussion

When the value of this property is `true`, the clock counts up from [`timeValue`](./timevalue.md) to show the elapsed time of the match or current period. When the value of this property is `false`, the clock counts down from the initial time to show the time remaining in the sports event or in the current period. The clock starts counting from the value you provide at initialization time. If the clock counts down, CarPlay automatically stops the countdown when the number of seconds reaches `0`. CarPlay doesn’t stop a clock that counts upward.

## See Also

### Getting the clock attributes
- [var timeValue: TimeInterval](./timevalue.md)
  The time value you specify at initialization.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the clock is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/countsup)*