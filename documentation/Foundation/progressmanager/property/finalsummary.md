# finalSummary(_:_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Determines how to handle summary data when a progress manager is deinitialized.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func finalSummary(_ parentSummary: Self.Summary, _ selfSummary: Self.Summary) -> Self.Summary
```

#### Return Value

The updated summary that replaces the parent’s current summary.

#### Discussion

This method is used when a progress manager in the hierarchy is being deinitialized and its accumulated summary needs to be processed in relation to its parent’s summary. The behavior can vary depending on the property type:

- For additive properties (like file counts, byte counts): The self summary is typically added to the parent summary to preserve the accumulated progress.
- For max-based properties (like estimated time remaining): The parent summary is typically preserved as it represents an existing estimate.
- For collection-based properties (like file URLs): The self summary may be discarded to avoid accumulating stale references.

## Parameters

- `parentSummary`: The current summary value of the parent progress manager.
- `selfSummary`: The final summary value from the progress manager being deinitialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property/finalsummary(_:_:))*