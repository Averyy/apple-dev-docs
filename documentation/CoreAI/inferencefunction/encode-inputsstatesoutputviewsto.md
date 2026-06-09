# encode(inputs:states:outputViews:to:)

**Framework**: Core AI  
**Kind**: method

Encodes the inference to the provided compute stream, returning async values for the outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func encode(inputs: [String : InferenceFunction.AsyncValue], states: consuming InferenceFunction.AsyncMutableViews = AsyncMutableViews(), outputViews: consuming InferenceFunction.AsyncMutableViews = AsyncMutableViews(), to stream: ComputeStream) throws -> [String : InferenceFunction.AsyncValue]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/encode(inputs:states:outputviews:to:))*