# countsUp

**Framework**: CarPlay  
**Kind**: property

If true, the timer is counting UP, so as to indicate an amount of time elapsed so far in this event.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
var countsUp: Bool { get }
```

#### Discussion

If false, the timer is counting DOWN, so as to indicate an amount of time remaining in the event, or a play period of the event (quarter/inning/period).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/countsup)*