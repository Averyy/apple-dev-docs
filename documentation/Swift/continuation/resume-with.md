# resume(with:)

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the continuation by having it either return or throw an error based on the state of the given `Result` value

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
consuming func resume(with result: consuming sending Result<Success, Failure>)
```

## Parameters

- `result`: A value to either return or throw from the continuation


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuation/resume(with:))*