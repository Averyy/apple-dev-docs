# previousAttemptCount

**Framework**: Network  
**Kind**: property

The number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.

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
let previousAttemptCount: Int
```

## See Also

- [let duration: TimeInterval](nwconnection/establishmentreport/duration.md)
  The total duration of the successful connection establishment attempt, from the preparing state to the ready state.
- [let attemptStartedAfterInterval: TimeInterval](nwconnection/establishmentreport/attemptstartedafterinterval.md)
  The time between the call to start and the beginning of the successful connection attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/previousattemptcount)*