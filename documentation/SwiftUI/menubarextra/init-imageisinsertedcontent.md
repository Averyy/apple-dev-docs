# init(_:image:isInserted:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 14.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>, @ViewBuilder content: () -> Content)
```

#### Discussion

The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

## Parameters

- `titleKey`: The localized string key to use for the accessibility   label of the item.
- `image`: The image resource to use as the label.
- `isInserted`: Whether the item is inserted in the menu bar. The item   may or may not be visible, depending on the number of items present.
- `content`: A   to display when the user selects the item.

## See Also

- [init(_:image:content:)](menubarextra/init(_:image:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](menubarextra/init(_:systemimage:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](menubarextra/init(_:systemimage:isinserted:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:isinserted:content:))*