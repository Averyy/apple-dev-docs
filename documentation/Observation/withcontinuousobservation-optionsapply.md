# withContinuousObservation(options:apply:)

**Framework**: Observation  
**Kind**: func

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func withContinuousObservation(options: ObservationTracking.Options, apply: @escaping @isolated(any) @Sendable (borrowing ObservationTracking.Event) -> Void) -> ObservationTracking.Token
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/withcontinuousobservation(options:apply:))*