# onDataEntry(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action whenever this dynamic profile produces a data entry.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
@export(implementation)
func onDataEntry(perform action: nonisolated(nonsending) sending @escaping () async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

**Other overloads**:

```swift
func onDataEntry(perform action: nonisolated(nonsending) sending @escaping (Transcript.DataEntry) async throws -> Void) -> some LanguageModelSession.DynamicProfile
```

## Discussion

Data entries are only produced by models that accept the entry’s content type through [`supportsDataEntryType(_:)`](../../languagemodel/supportsdataentrytype%28_%29.md).

When the `onDataEntry` closure throws an error, the caller’s `respond` or `response` propagates that error.

Use this to observe or log the custom data the model produces as it works toward a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/ondataentry(perform:))*