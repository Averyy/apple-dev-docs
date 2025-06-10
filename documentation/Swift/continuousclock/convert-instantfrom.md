# convert(instant:from:)

**Framework**: Swift  
**Kind**: method

Convert an `Instant` from some other clock’s `Instant`

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
func convert<OtherClock>(instant: OtherClock.Instant, from clock: OtherClock) -> Self.Instant? where OtherClock : Clock
```

#### Discussion

Parameters:

- instant:    The instant to convert.

Returns: An `Instant` representing the equivalent instant, or `nil` if this function is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/convert(instant:from:))*