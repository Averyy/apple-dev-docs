# init(elapsedTime:paused:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a clock that counts up to measure the elapsed time from the specified value.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(elapsedTime: TimeInterval, paused: Bool)
```

```objc
- (instancetype) initWithElapsedTime:(NSTimeInterval) elapsedTime paused:(BOOL) paused;
```

## Discussion

Use this method for sports events in which the game clock counts up from `0`. After updating the Now Playing interface with this information, CarPlay starts the clock if the `paused` parameter is `false`.

## Parameters

- `elapsedTime`: The number of elapsed seconds in the match. Specify `0` to represent the start of the match.
- `paused`: `true` to prevent CarPlay from incrementing the time value automatically, or `false` to start counting up.

## See Also

### Creating a sports mode type
- [init(timeRemaining: TimeInterval, paused: Bool)](./init%28timeremaining,paused%29.md)
  Creates a clock that counts down from the specified value.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/init(elapsedtime:paused:))*