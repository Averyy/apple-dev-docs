# Output

**Framework**: Foundation Models  
**Kind**: associatedtype  
**Required**: Yes

The output that this tool produces for the language model to reason about in subsequent interactions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Output : PromptRepresentable
```

#### Discussion

Typically output is either a `String` or a [`Generable`](generable.md) type.

## See Also

- [func call(arguments: Self.Arguments) async throws -> Self.Output](tool/call(arguments:).md)
  Performs the tool’s action when a language model wants to use this tool.
- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/output)*