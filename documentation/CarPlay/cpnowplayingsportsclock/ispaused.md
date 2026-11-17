# isPaused

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the clock is paused.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var isPaused: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isPaused) BOOL paused;
```

## Discussion

When the value of this property is `true`, CarPlay holds the clock at the value in [`timeValue`](./timevalue.md) and doesn’t increment or decrement it. When the value of this property is `false`, CarPlay updates the clock every second, counting up or down based on the clock’s configuration.

## See Also

### Getting the clock attributes
- [var timeValue: TimeInterval](./timevalue.md)
  The time value you specify at initialization.
- [var countsUp: Bool](./countsup.md)
  A Boolean value that indicates whether the event clock counts up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/ispaused)*