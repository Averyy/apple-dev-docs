# convert(from:)

**Framework**: Swift  
**Kind**: method

Convert a Swift Duration to a Clock-specific Duration

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
func convert(from duration: Duration) -> Self.Duration?
```

#### Discussion

Parameters:

- from duration: The `Swift.Duration` to convert.

Returns: A `Duration` representing the equivalent duration, or `nil` if this function is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/convert(from:)-3lfde)*