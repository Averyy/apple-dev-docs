# analyze(for:)

**Framework**: Music Understanding  
**Kind**: method

Performs the specified analyses on the session’s audio source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func analyze(for analysisTypes: Set<AnalysisType>) async throws -> MusicUnderstandingSession.SessionResult
```

#### Return Value

The aggregated session result containing all requested analyses.

#### Discussion

> **Note**:  If the analysis types set is empty, or if analysis is already running on this session.

> **Note**:  Call this method only once per session instance. Create a new session to run additional analyses.

Example usage:

```swift
let session = MusicUnderstandingSession(audioProvider: provider)
let result = try await session.analyze(for: [.rhythm, .pace, .loudness])
```

## Parameters

- `analysisTypes`: A `Set` of `AnalysisType` values specifying which analyses to perform.

## See Also

- [func analyze() async throws -> MusicUnderstandingSession.SessionResult](musicunderstandingsession/analyze.md)
  Performs all available analyses on the session’s audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/analyze(for:))*