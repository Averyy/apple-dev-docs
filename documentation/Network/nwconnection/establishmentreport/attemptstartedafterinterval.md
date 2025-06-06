# attemptStartedAfterInterval

**Framework**: Network  
**Kind**: property

The time between the call to start and the beginning of the successful connection attempt.

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
let attemptStartedAfterInterval: TimeInterval
```

## See Also

- [let duration: TimeInterval](nwconnection/establishmentreport/duration.md)
  The total duration of the successful connection establishment attempt, from the preparing state to the ready state.
- [let previousAttemptCount: Int](nwconnection/establishmentreport/previousattemptcount.md)
  The number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/establishmentreport/attemptstartedafterinterval)*