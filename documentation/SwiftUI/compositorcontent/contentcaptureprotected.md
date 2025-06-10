# contentCaptureProtected(_:)

**Framework**: SwiftUI  
**Kind**: method

Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func contentCaptureProtected(_ isActive: Bool = true) -> some CompositorContent
```

#### Discussion

On visionOS, the system redacts the entire screen when a view marked with this modifier is present on screen, scene capture is active, and the app has the App Protected Content entitlement, available through the Apple Developer Enterprise Program.

## Parameters

- `isActive`: A Boolean value that specifies   whether this view is protected when present on   screen during scene capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/contentcaptureprotected(_:))*