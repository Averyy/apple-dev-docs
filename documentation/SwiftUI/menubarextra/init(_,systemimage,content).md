# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, systemImage: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

#### Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleResource`: The localized string resource to use for the accessibility label of the item.
- `systemImage`: The name of a system image to use as the label.
- `content`: A `View` to display when the user selects the item.

## See Also

### Creating a menu bar extra with an image
- [init(_:image:content:)](./init%28_,image,content%29.md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:image:isInserted:content:)](./init%28_,image,isinserted,content%29.md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](./init%28_,systemimage,isinserted,content%29.md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:systemimage:content:))*