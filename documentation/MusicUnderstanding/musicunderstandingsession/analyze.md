# analyze()

**Framework**: Music Understanding  
**Kind**: method

Performs all available analyses on the session’s audio source.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
func analyze() async throws -> MusicUnderstandingSession.SessionResult
```

#### Return Value

The aggregated session result containing all analyses.

#### Discussion

> **Note**:  If analysis is already running on this session.

> **Note**:  This method can only be called once per session instance. Create a new session to run additional analyses.

Example usage:

```swift
let session = MusicUnderstandingSession(audioProvider: provider)
let result = try await session.analyze()
```

## See Also

- [func analyze(for: Set<AnalysisType>) async throws -> MusicUnderstandingSession.SessionResult](musicunderstandingsession/analyze(for:).md)
  Performs the specified analyses on the session’s audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/analyze())*