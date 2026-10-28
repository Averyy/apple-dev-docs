# subscript(_:)

**Framework**: Foundation Models  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the entry at the specified position in the history view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(position: Transcript.HistoryView.Index) -> Transcript.Entry { get set }
```

**Other overloads**:

```swift
subscript(bounds: Range<Transcript.HistoryView.Index>) -> Transcript.HistoryView { get set }
```

## Parameters

- `position`: The position of the entry to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/historyview/subscript(_:)-5jzcz)*