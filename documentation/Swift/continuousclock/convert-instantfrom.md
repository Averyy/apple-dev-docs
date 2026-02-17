# convert(instant:from:)

**Framework**: Swift  
**Kind**: method

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
func convert<OtherClock>(instant: OtherClock.Instant, from clock: OtherClock) -> Self.Instant? where OtherClock : Clock
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/convert(instant:from:))*