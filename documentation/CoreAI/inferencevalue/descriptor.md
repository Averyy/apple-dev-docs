# InferenceValue.Descriptor

**Framework**: Core AI  
**Kind**: enum

A description of the type and shape of an inference value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Descriptor
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

You obtain descriptors from [`InferenceFunctionDescriptor`](inferencefunctiondescriptor.md) to inspect what kind of value a function expects for each input or output.

## Topics

### Defining value descriptors
- [InferenceValue.Descriptor.image(_:)](inferencevalue/descriptor/image(_:).md)
- [InferenceValue.Descriptor.ndArray(_:)](inferencevalue/descriptor/ndarray(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [InferenceValue.Kind](inferencevalue/kind-swift.enum.md)
  The type of data an inference value contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/descriptor)*