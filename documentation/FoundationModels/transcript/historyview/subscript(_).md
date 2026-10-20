# subscript(_:)

**Framework**: Foundation Models  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the subsequence of entries within the specified bounds.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(bounds: Range<Transcript.HistoryView.Index>) -> Transcript.HistoryView { get set }
```

**Other overloads**:

```swift
subscript(position: Transcript.HistoryView.Index) -> Transcript.Entry { get set }
```

## Parameters

- `bounds`: A range of valid indices in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/historyview/subscript(_:))*