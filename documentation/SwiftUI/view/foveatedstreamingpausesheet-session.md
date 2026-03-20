# foveatedStreamingPauseSheet(session:)

**Framework**: SwiftUI  
**Kind**: method

Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency func foveatedStreamingPauseSheet(session: Binding<FoveatedStreamingSession?>) -> some View
```

#### Discussion

Add this view modifier to inform the system that it should display UI for resuming the foveated streaming session when the person pauses the session. Otherwise, build your own UI that allows the person to resume the session by calling the `FoveatedStreamingSession/resume()` function.

## Parameters

- `session`: A binding to the foveated streaming session to display the pause sheet for. If `nil`, the system never displays the pause sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foveatedstreamingpausesheet(session:))*