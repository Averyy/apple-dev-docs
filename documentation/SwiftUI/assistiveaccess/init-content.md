# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a Assistive Access scene.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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