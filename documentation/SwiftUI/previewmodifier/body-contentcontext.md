# body(content:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Modify a preview by applying the shared context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@ViewBuilder
@MainActor func body(content: Self.Content, context: Self.Context) -> Self.Body
```

## Parameters

- `content`: A proxy for the preview being modified.
- `context`: The shared context to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewmodifier/body(content:context:))*