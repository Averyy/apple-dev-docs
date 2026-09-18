# init(isEnabled:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a scene accessory that presents content during camera capture, with a binding for programmatic enablement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
init(isEnabled: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `isEnabled`: A binding for whether or not the accessory should present if available.
- `content`: The scene’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory/init(isenabled:content:))*