# sleep(for:tolerance:)

**Framework**: Swift  
**Kind**: method

Suspends for the given duration.

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
func sleep(for duration: Self.Instant.Duration, tolerance: Self.Instant.Duration? = nil) async throws
```

#### Discussion

Prefer to use the `sleep(until:tolerance:)` method on `Clock` if you have access to an absolute instant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/suspendingclock/sleep(for:tolerance:))*