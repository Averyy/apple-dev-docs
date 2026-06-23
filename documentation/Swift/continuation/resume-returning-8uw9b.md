# resume(returning:)

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the continuation by having it return from its suspension point

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
consuming func resume(returning value: consuming sending Success) where Failure == Never
```

## Parameters

- `value`: The value to return from the continuation


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuation/resume(returning:)-8uw9b)*