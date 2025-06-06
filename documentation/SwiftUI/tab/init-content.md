# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new tab that you can use in a tab view, with an empty label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(@ViewBuilder content: () -> Content) where Label == EmptyView
```

## Parameters

- `content`: The view content of the tab.

## See Also

- [init(value:content:)](tab/init(value:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(role: TabRole?, content: () -> Content)](tab/init(role:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](tab/init(value:role:content:).md)
  Creates a new tab with a label inferred from the role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(content:))*