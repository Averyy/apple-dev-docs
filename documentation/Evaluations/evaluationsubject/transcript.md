# transcript

**Framework**: Evaluations  
**Kind**: property  
**Required**: Yes

The structured transcript captured while producing the value, if any.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var transcript: StructuredTranscript? { get }
```

#### Discussion

Subjects backed by a language model session expose the session transcript here; subjects that don’t involve a model leave it `nil` (the default). The transcript-attachment recorder reads this through the type-erased results column, so any subject type that carries one participates automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationsubject/transcript)*