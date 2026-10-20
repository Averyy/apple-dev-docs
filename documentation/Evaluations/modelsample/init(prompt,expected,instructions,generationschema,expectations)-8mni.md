# init(prompt:expected:instructions:generationSchema:expectations:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a model sample with a FoundationModels prompt.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(prompt: Prompt, expected: ExpectedValue? = Optional<String>(nilLiteral: ()), instructions: Instructions? = nil, generationSchema: GenerationSchema? = nil, expectations: TrajectoryExpectation? = nil)
```

## See Also

### Creating a sample
- [init(prompt: String, expected: ExpectedValue?, instructions: String?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](./init%28prompt,expected,instructions,generationschema,expectations%29-7daed.md)
  Creates a model sample with string-based prompt and instructions.
- [init(input: ModelSampleInput, expected: ExpectedValue?, expectations: TrajectoryExpectation?)](./init%28input,expected,expectations%29.md)
  Creates a model sample with a prebuilt input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/init(prompt:expected:instructions:generationschema:expectations:)-8mni)*