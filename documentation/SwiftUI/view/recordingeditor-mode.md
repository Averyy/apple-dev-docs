# recordingEditor(_:mode:)

**Framework**: SwiftUI  
**Kind**: method

Presents the recording editor for the given recording URL with a specific mode.

**Availability**:
- tvOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func recordingEditor(_ item: Binding<URL?>, mode: SCRecordingEditor.Mode) -> some View
```

## Parameters

- `item`: A binding to an optional URL. Non-nil presents the editor; nil dismisses it.
- `mode`: The editor mode (`.preview` or `.share`).

## See Also

- [func recordingEditor(Binding<URL?>) -> some View](view/recordingeditor(_:).md)
  Presents the recording editor for the given recording URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/recordingeditor(_:mode:))*