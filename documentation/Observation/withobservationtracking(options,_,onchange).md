# withObservationTracking(options:_:onChange:)

**Framework**: Observation  
**Kind**: func

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func withObservationTracking<Result, Failure>(options: ObservationTracking.Options, _ apply: () throws(Failure) -> Result, onChange: @escaping @Sendable (borrowing ObservationTracking.Event) -> Void) throws(Failure) -> Result where Failure : Error, Result : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/withobservationtracking(options:_:onchange:))*