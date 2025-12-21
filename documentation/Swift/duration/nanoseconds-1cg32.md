# nanoseconds(_:)

**Framework**: Swift  
**Kind**: method

Construct a `Duration` given a number of seconds nanoseconds as a `Double` by converting the value into the closest attosecond scale value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func nanoseconds(_ nanoseconds: Double) -> Duration
```

#### Return Value

A `Duration` representing a given number of nanoseconds.

#### Discussion

```swift
  let d: Duration = .nanoseconds(382.9)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/nanoseconds(_:)-1cg32)*