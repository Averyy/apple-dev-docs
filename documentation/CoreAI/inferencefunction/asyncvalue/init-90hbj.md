# init(_:)

**Framework**: Core AI  
**Kind**: init

Initialize an async value from an existing mutable async value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ mutableValue: consuming InferenceFunction.AsyncMutableValue)
```

## Parameters

- `mutableValue`: The mutable value that this value will be initialized from. The resulting value will reference the same underlying value within the mutable value and carry the same event to signal when the value is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/init(_:)-90hbj)*