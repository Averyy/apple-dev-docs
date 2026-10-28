# setContext(_:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Sets contextual information to improve or inform the analysis.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func setContext(_ newContext: AnalysisContext) async throws
```

## Discussion

Other analyzer instances may use the same context object.

## Parameters

- `newContext`: A context object. This object will replace the current object.

## See Also

### Managing contexts
- [var context: AnalysisContext](./context.md)
  An object containing contextual information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/setcontext(_:))*