# measure(isolation:_:)

**Framework**: Swift  
**Kind**: method

Measure the elapsed time to execute an asynchronous closure.

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
func measure(isolation: isolated (any Actor)? = #isolation, _ work: () async throws -> Void) async rethrows -> Self.Instant.Duration
```

#### Discussion

```swift
  let clock = ContinuousClock()
  let elapsed = await clock.measure {
     await someWork()
  }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/measure(isolation:_:))*