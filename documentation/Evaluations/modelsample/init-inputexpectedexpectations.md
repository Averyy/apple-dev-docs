# init(input:expected:expectations:)

**Framework**: Evaluations  
**Kind**: init

Creates a model sample with a prebuilt input.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(input: ModelSampleInput, expected: ExpectedValue? = Optional<String>(nilLiteral: ()), expectations: TrajectoryExpectation? = nil)
```

## See Also

- [init(prompt: String, expected: ExpectedValue?, instructions: String?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](modelsample/init(prompt:expected:instructions:generationschema:expectations:)-7daed.md)
  Creates a model sample with string-based prompt and instructions.
- [init(prompt: Prompt, expected: ExpectedValue?, instructions: Instructions?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](modelsample/init(prompt:expected:instructions:generationschema:expectations:)-8mni.md)
  Creates a model sample with a FoundationModels prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/init(input:expected:expectations:))*