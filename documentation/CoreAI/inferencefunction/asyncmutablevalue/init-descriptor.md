# init(descriptor:)

**Framework**: Core AI  
**Kind**: init

Initialize a new state by creating a value matching the provided descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(descriptor: consuming InferenceValue.Descriptor)
```

#### Discussion

Note that the descriptor must not have a dynamic shape.

## Parameters

- `descriptor`: The descriptor of the inference value to be constructed and held by this state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(descriptor:))*