# onDisappear(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform after this content disappears.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onDisappear(perform action: (() -> Void)? = nil) -> some CompositorContent
```

#### Return Value

A CompositorContent that triggers `action` after it disappears.

#### Discussion

The exact moment that SwiftUI calls this method depends on the specific content type that you apply it to, but the `action` closure doesn’t execute until the content disappears from the interface.

## Parameters

- `action`: The action to perform. If   is  , the   call has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/ondisappear(perform:))*