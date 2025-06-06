# continuous

**Framework**: Swift  
**Kind**: property

A clock that measures time that always increments but does not stop incrementing while the system is asleep.

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
static var continuous: ContinuousClock { get }
```

#### Discussion

```swift
  try await Task.sleep(until: .now + .seconds(3), clock: .continuous)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clock/continuous)*