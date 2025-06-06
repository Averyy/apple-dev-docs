# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra with a key for a localized string to use as the label. The extra defines the primary scene of an `App`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ViewBuilder content: () -> Content)
```

#### Discussion

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleKey`: The title key to use for the label of the item.
- `content`: A   to display when the user selects the item.

## See Also

- [init(content: () -> Content, label: () -> Label)](menubarextra/init(content:label:).md)
  Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](menubarextra/init(_:isinserted:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
- [init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)](menubarextra/init(isinserted:content:label:).md)
  Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:content:))*