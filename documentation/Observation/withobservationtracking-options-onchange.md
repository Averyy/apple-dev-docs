# withObservationTracking(options:_:onChange:)

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
func withObservationTracking<Result, Failure>(options: ObservationTracking.Options, _ apply: () throws(Failure) -> Result, onChange: @escaping @Sendable (borrowing ObservationTracking.Event) -> Void) throws(Failure) -> Result where Failure : Error, Result : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/withobservationtracking(options:_:onchange:))*