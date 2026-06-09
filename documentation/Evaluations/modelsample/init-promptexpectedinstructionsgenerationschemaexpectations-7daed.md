# init(prompt:expected:instructions:generationSchema:expectations:)

**Framework**: Evaluations  
**Kind**: init

Creates a model sample with string-based prompt and instructions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(prompt: String, expected: ExpectedValue? = Optional<String>(nilLiteral: ()), instructions: String? = nil, generationSchema: GenerationSchema? = nil, expectations: TrajectoryExpectation? = nil)
```

## See Also

- [init(prompt: Prompt, expected: ExpectedValue?, instructions: Instructions?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](modelsample/init(prompt:expected:instructions:generationschema:expectations:)-8mni.md)
  Creates a model sample with a FoundationModels prompt.
- [init(input: ModelSampleInput, expected: ExpectedValue?, expectations: TrajectoryExpectation?)](modelsample/init(input:expected:expectations:).md)
  Creates a model sample with a prebuilt input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/init(prompt:expected:instructions:generationschema:expectations:)-7daed)*