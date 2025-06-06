# init(action:)

**Framework**: App Intents  
**Kind**: init

Creates a link that launches Shortcuts and then executes the specified closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(action: @escaping () -> Void = {})
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/init(action:))*