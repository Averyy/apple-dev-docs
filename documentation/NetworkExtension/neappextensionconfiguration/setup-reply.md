# setup(reply:)

**Framework**: Network Extension  
**Kind**: method

Sets up the app extension.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func setup(reply: @escaping (Bool) -> Void)
```

#### Discussion

The framework calls this method. You don’t need to call it in your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration/setup(reply:))*