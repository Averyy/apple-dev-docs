# init(isInserted:content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(isInserted: Binding<Bool>, @ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `isInserted`: Whether the item is inserted in the menu bar.   The item may or may not be visible, depending on the number of items   present.
- `content`: A   to display when the user selects the item.
- `label`: A   to use as the label in the system menu bar.

## See Also

- [init(_:content:)](menubarextra/init(_:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The extra defines the primary scene of an `App`.
- [init(content: () -> Content, label: () -> Label)](menubarextra/init(content:label:).md)
  Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](menubarextra/init(_:isinserted:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(isinserted:content:label:))*