# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a hosting configuration with the given contents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(@ContentBuilder content: () -> Content)
```

Available when `Content` conforms to `View` and `Background` is `EmptyView`.

## Parameters

- `content`: The contents of the SwiftUI hierarchy to be shown inside the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/init(content:))*