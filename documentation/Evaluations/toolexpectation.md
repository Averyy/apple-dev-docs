# ToolExpectation

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A specification for an expected tool call, or a group of expectations that can be satisfied in any order.

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
struct ToolExpectation
```

## Mentions

- [Evaluating language model responses](./evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](./evaluating-tool-calling-behavior.md)

## Overview

Most commonly, a `ToolExpectation` identifies a single tool by name and optionally validates its arguments:

```swift
ToolExpectation("getWeather", arguments: [
    .exact(argumentName: "location", value: "Paris, France")
])
```

For ordered sequences where multiple tools must all be called at the same position but their relative order doesn’t matter, use [`anyOrder(_:)`](./toolexpectation/anyorder%28_%29.md):

```swift
ToolExpectation.anyOrder([
    ToolExpectation("fetchData"),
    ToolExpectation("fetchMetadata"),
])
```

## Topics

### Creating an expectation
- [init(String, arguments: [ArgumentMatcher])](./toolexpectation/init%28_,arguments%29.md)
  Creates a new tool expectation.
### Creating any-order groups
- [static func anyOrder([ToolExpectation]) -> ToolExpectation](./toolexpectation/anyorder%28_%29.md)
  Creates a group of expectations that must all be satisfied at the same sequential position, but can occur in any relative order.
### Accessing expectation details
- [var name: String](./toolexpectation/name.md)
  The name of the tool that the evaluation expects the model to call.
- [var arguments: [ArgumentMatcher]](./toolexpectation/arguments.md)
  The argument matchers to validate against the tool call.
- [var isAnyOrderGroup: Bool](./toolexpectation/isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.
### Matching arguments
- [enum ArgumentMatcher](./argumentmatcher.md)
  The values that define how to validate a tool-call argument.
### Initializers
- [init(from: any Decoder) throws](./toolexpectation/init%28from%29.md)
  Creates a tool expectation by decoding from the given decoder.
### Instance Properties
- [var generatedContent: GeneratedContent](./toolexpectation/generatedcontent.md)
  The generated content representation of this tool expectation.
### Instance Methods
- [func encode(to: any Encoder) throws](./toolexpectation/encode%28to%29.md)
  Encodes this tool expectation into the given encoder.
### Type Properties
- [static var generationSchema: GenerationSchema](./toolexpectation/generationschema.md)
  The generation schema for this tool expectation.
### Enumerations
- [ToolExpectation.PartiallyGenerated](./toolexpectation/partiallygenerated.md)
  A partially generated form of a tool expectation.
### Default Implementations
- [ConvertibleFromGeneratedContent Implementations](./toolexpectation/convertiblefromgeneratedcontent-implementations.md)

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../FoundationModels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/convertibletogeneratedcontent.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [Generable](../FoundationModels/generable.md)
- [InstructionsRepresentable](../FoundationModels/instructionsrepresentable.md)
- [PromptRepresentable](../FoundationModels/promptrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a single-tool expectation
- [init(expected: String, arguments: [ArgumentMatcher])](./trajectoryexpectation/init%28expected,arguments%29.md)
  Creates a trajectory expectation for a single expected tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation)*