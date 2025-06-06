# init(value:role:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new tab with a label inferred from the role.

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
nonisolated
init(value: Value, role: TabRole?, @ViewBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `value`: The   value which selects this tab.
- `role`: The   defining the semantic purpose of the tab.
- `content`: The view content of the tab.

## See Also

- [init(content: () -> Content)](tab/init(content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:content:)](tab/init(value:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(role: TabRole?, content: () -> Content)](tab/init(role:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(value:role:content:))*