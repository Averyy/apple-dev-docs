# init(catching:)

**Framework**: Swift  
**Kind**: init

Creates a new result by evaluating a throwing closure, capturing the returned value as a success, or any thrown error as a failure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(catching body: () throws(Failure) -> Success)
```

## Parameters

- `body`: A potentially throwing closure to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/init(catching:)-62kyq)*