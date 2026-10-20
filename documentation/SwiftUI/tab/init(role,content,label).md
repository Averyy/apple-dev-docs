# init(role:content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(role: TabRole?, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

Available when `Value` is `Never`, `Content` conforms to `View`, and `Label` conforms to `View`.

## Parameters

- `role`: The role defining the semantic purpose of the tab.
- `content`: The view content of the tab.
- `label`: The label for the tab’s tab item.

## See Also

### Creating a tab with label
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a new tab with a label that you can use in a tab view.
- [init(value:content:label:)](./init%28value,content,label%29.md)
  Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](./init%28value,role,content,label%29.md)
  Creates a new tab with a label that you can use in a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(role:content:label:))*