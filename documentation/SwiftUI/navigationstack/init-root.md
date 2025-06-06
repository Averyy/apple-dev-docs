# init(root:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation stack that manages its own navigation state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder root: () -> Root) where Data == NavigationPath
```

## Parameters

- `root`: The view to display when the stack is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationstack/init(root:))*