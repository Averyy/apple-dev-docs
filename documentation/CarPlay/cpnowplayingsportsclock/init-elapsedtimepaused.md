# init(elapsedTime:paused:)

**Framework**: CarPlay  
**Kind**: init

Represents a duration of time that has elapsed so far in this event, or play period of the event (quarter/inning/period).

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
init(elapsedTime: TimeInterval, paused: Bool)
```

#### Discussion

When displayed on the now playing screen, the clock will count UP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/init(elapsedtime:paused:))*