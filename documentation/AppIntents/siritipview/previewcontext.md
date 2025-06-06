# previewContext(_:)

**Framework**: App Intents  
**Kind**: method

Declares a context for the preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func previewContext<C>(_ value: C) -> some View where C : PreviewContext
```

## Parameters

- `value`: The context for the preview; the default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/previewcontext(_:))*