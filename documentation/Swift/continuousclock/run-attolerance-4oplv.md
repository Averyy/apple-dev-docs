# run(_:at:tolerance:)

**Framework**: Swift  
**Kind**: method

Run the given job on an unspecified executor at some point after the given instant.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
func run(_ job: consuming ExecutorJob, at instant: Self.Instant, tolerance: Self.Duration?)
```

#### Discussion

Parameters:

- job:         The job we wish to run
- at instant:  The time at which we would like it to run.
- tolerance:   The ideal maximum delay we are willing to tolerate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/run(_:at:tolerance:)-4oplv)*