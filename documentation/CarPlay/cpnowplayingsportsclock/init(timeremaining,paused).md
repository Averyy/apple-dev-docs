# init(timeRemaining:paused:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Represents an amount of time remaining in the event, or play period of the event (quarter/inning/period).

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

When displayed on the now playing screen, the clock will count DOWN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/init(timeremaining:paused:))*