# init(isEnabled:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a scene accessory that presents non-interactive content on an external display with a binding for programmatic enablement.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(isEnabled: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `isEnabled`: A binding for whether or not the accessory should present if available.
- `content`: The scene’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory/init(isenabled:content:))*