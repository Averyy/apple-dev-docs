# recordingEditor(_:)

**Framework**: SwiftUI  
**Kind**: method

Presents the recording editor for the given recording URL.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func recordingEditor(_ item: Binding<URL?>) -> some View
```

#### Discussion

When `item` is non-nil, the editor is presented for that URL. When the user dismisses, the framework sets `item` back to `nil`.

```swift
.recordingEditor($recordingURL)
```

## Parameters

- `item`: A binding to an optional URL. Non-nil presents the editor; nil dismisses it.

## See Also

- [func recordingEditor(Binding<URL?>, mode: SCRecordingEditor.Mode) -> some View](view/recordingeditor(_:mode:).md)
  Presents the recording editor for the given recording URL with a specific mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/recordingeditor(_:))*