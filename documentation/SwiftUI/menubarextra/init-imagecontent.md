# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 14.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, @ViewBuilder content: () -> Content)
```

#### Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleKey`: The localized string key to use for the accessibility   label of the item.
- `image`: The image resource to use as the label.
- `content`: A   to display when the user selects the item.

## See Also

- [init(_:image:isInserted:content:)](menubarextra/init(_:image:isinserted:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](menubarextra/init(_:systemimage:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](menubarextra/init(_:systemimage:isinserted:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:content:))*