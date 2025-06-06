# measure(_:)

**Framework**: Swift  
**Kind**: method

Measure the elapsed time to execute a closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func measure(_ work: () throws -> Void) rethrows -> Self.Instant.Duration
```

#### Discussion

```swift
  let clock = ContinuousClock()
  let elapsed = clock.measure {
     someWork()
  }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clock/measure(_:))*