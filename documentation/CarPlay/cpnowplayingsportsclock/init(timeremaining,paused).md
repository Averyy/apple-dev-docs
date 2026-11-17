# init(timeRemaining:paused:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a clock that counts down from the specified value.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(timeRemaining: TimeInterval, paused: Bool)
```

```objc
- (instancetype) initWithTimeRemaining:(NSTimeInterval) timeRemaining paused:(BOOL) paused;
```

## Discussion

Use this method for sports events in which the game clock counts down for the current period or the overall match. After updating the Now Playing interface with this information, CarPlay starts the clock if the `paused` parameter is `false`.

## Parameters

- `timeRemaining`: The number of seconds remaining in the match or period.
- `paused`: `true` to prevent CarPlay from decrementing the time value automatically, or `false` to start counting down.

## See Also

### Creating a sports mode type
- [init(elapsedTime: TimeInterval, paused: Bool)](./init%28elapsedtime,paused%29.md)
  Creates a clock that counts up to measure the elapsed time from the specified value.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/init(timeremaining:paused:))*