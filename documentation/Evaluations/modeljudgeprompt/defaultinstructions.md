# defaultInstructions

**Framework**: Evaluations  
**Kind**: property  
**Role**: Type Property

The default system instructions used when no custom instructions are provided.

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

### Creating a prompt configuration
- [init(instructions: String, evaluationTarget: ((Input.ExpectedValue) -> String)?, reference: ((Input, Input.ExpectedValue) async throws -> [String : String])?)](./init%28instructions,evaluationtarget,reference%29.md)
  Creates a model prompt configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeprompt/defaultinstructions)*