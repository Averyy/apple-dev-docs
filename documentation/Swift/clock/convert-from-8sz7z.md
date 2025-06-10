# convert(from:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Convert a Clock-specific Duration to a Swift Duration

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
func convert(from duration: Self.Duration) -> Duration?
```

#### Discussion

Some clocks may define `C.Duration` to be something other than a `Swift.Duration`, but that makes it tricky to convert timestamps between clocks, which is something we want to be able to support. This method will convert whatever `C.Duration` is to a `Swift.Duration`.

Parameters:

- from duration: The `Duration` to convert

Returns: A `Swift.Duration` representing the equivalent duration, or `nil` if this function is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clock/convert(from:)-8sz7z)*