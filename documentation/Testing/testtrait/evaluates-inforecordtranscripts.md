# evaluates(_:info:recordTranscripts:)

**Framework**: Swift Testing  
**Kind**: method

Creates a trait that runs a single evaluation and makes its result available through the current evaluation context.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static func evaluates(_ evaluation: any Evaluation, info: [String : String] = [:], recordTranscripts: Bool = false) -> Self
```

## Parameters

- `evaluation`: The evaluation to run.
- `info`: User-defined key-value pairs attached to the result, such as model name or dataset version.
- `recordTranscripts`: When `true`, each row’s transcript snapshot is embedded in the `.xcevalresult` attachment under the `Transcript` column. Recoverable on load via `EvaluationResult/transcriptSnapshots`. Defaults to `false` so the attachment stays small for runs that don’t need transcripts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/testtrait/evaluates(_:info:recordtranscripts:))*