# init(value:content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new tab with a label that you can use in a tab view.

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
init(value: Value, @ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `value`: The   value which selects this tab.
- `content`: The view content of the tab.
- `label`: The label for the tab’s tab item.

## See Also

- [init(content: () -> Content, label: () -> Label)](tab/init(content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
- [init(role: TabRole?, content: () -> Content, label: () -> Label)](tab/init(role:content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](tab/init(value:role:content:label:).md)
  Creates a new tab with a label that you can use in a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(value:content:label:))*