# isPaused

**Framework**: CarPlay  
**Kind**: property

Whether the clock should be paused, e.g. due to a stoppage in play.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
var isPaused: Bool { get }
```

#### Discussion

If YES, the clock will be paused at the specified value.

If NO, the clock will count up (or down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/ispaused)*