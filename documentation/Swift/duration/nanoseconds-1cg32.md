# nanoseconds(_:)

**Framework**: Swift  
**Kind**: method

Construct a `Duration` given a number of seconds nanoseconds as a `Double` by converting the value into the closest attosecond scale value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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