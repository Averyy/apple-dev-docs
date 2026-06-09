# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that can perform programmatic scrolling of its child scroll views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder content: @escaping (ScrollViewProxy) -> Content)
```

## Parameters

- `content`: The reader’s content, containing one or more scroll views. This content builder receives a [`ScrollViewProxy`](scrollviewproxy.md) instance that you use to perform scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollviewreader/init(content:))*