# init(catching:)

**Framework**: Swift  
**Kind**: init

Creates a new result by evaluating an async throwing closure, capturing the returned value as a success, or any thrown error as a failure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
(nonsending) init(catching body: nonisolated(nonsending) () async throws(Failure) -> Success) async
```

## Parameters

- `body`: A potentially throwing async closure to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/init(catching:)-1tno)*