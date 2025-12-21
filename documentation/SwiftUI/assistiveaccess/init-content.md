# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an Assistive Access scene.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(@ViewBuilder content: () -> Content)
```

#### Discussion

When Assistive Access is enabled, the given view is used as the root view of the app.

## Parameters

- `content`: A closure that creates the content for the   app when Assistive Access is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/assistiveaccess/init(content:))*