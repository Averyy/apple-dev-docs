# onAppear(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform before this content appears.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onAppear(perform action: (() -> Void)? = nil) -> some CompositorContent
```

#### Return Value

A CompositorContent that triggers `action` before it appears.

#### Discussion

The exact moment that SwiftUI calls this method depends on the specific content type that you apply it to, but the `action` closure completes before the first rendered frame appears.

## Parameters

- `action`: The action to perform. If   is  , the   call has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/onappear(perform:))*