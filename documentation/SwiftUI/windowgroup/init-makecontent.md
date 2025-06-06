# init(makeContent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a window group.

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
init(@ViewBuilder makeContent: @escaping () -> Content)
```

#### Discussion

The window group uses the given view as a template to form the content of each window in the group.

## Parameters

- `makeContent`: A closure that creates the content for each   instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(makecontent:))*