# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(@ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

#### Discussion

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `content`: A   to display when the user selects the item.
- `label`: A   to use as the label in the system menu bar.

## See Also

- [init(_:content:)](menubarextra/init(_:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The extra defines the primary scene of an `App`.
- [init(_:isInserted:content:)](menubarextra/init(_:isinserted:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
- [init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)](menubarextra/init(isinserted:content:label:).md)
  Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(content:label:))*