# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, @ViewBuilder content: () -> Content)
```

#### Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleKey`: The localized string key to use for the accessibility   label of the item.
- `systemImage`: The name of a system image to use as the label.
- `content`: A   to display when the user selects the item.

## See Also

- [init(_:image:content:)](menubarextra/init(_:image:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:image:isInserted:content:)](menubarextra/init(_:image:isinserted:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](menubarextra/init(_:systemimage:isinserted:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:systemimage:content:))*