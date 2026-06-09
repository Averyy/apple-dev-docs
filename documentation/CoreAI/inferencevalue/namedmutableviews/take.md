# take(_:)

**Framework**: Core AI  
**Kind**: method

Takes the mutable view for the specified value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func take(_ valueName: String) -> InferenceValue.MutableView?
```

#### Return Value

A mutable view of the value, or `nil` if no value with the specified name exists.

#### Discussion

Each value can only be taken once. Requesting the same value again produces a fatal error.

## Parameters

- `valueName`: The name of the value to take.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/namedmutableviews/take(_:))*