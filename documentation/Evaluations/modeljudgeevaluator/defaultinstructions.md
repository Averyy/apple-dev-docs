# defaultInstructions

**Framework**: Evaluations  
**Kind**: property  
**Role**: Type Property

The default system instructions the model uses when no custom instructions are provided.

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
static var defaultInstructions: String { get }
```

## See Also

### Configuring the judge prompt
- [func judgePrompt(for: Input, output: Input.ExpectedValue) async throws -> Prompt](./judgeprompt%28for,output%29.md)
  Builds and returns the full judge prompt for inspection, debugging, or logging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator/defaultinstructions)*