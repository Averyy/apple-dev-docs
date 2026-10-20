# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label representing a family activity application.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+

## Declaration

```swift
nonisolated
init(_ applicationToken: ApplicationToken)
```

Available when `Title` is `FamilyActivityTitleView` and `Icon` is `FamilyActivityIconView`.

**Other overloads**:

```swift
nonisolated
init(_ categoryToken: ActivityCategoryToken)
```

```swift
nonisolated
init(_ configuration: LabelStyleConfiguration)
```

```swift
nonisolated
init(_ webDomainToken: WebDomainToken)
```

## See Also

### Creating a label
- [init(_:image:)](./init%28_,image%29.md)
  Creates a label with an icon image and a title generated from a localized string.
- [init(_:systemImage:)](./init%28_,systemimage%29.md)
  Creates a label with a system icon image and a title generated from a localized string.
- [init(title: () -> Title, icon: () -> Icon)](./init%28title,icon%29.md)
  Creates a label with a custom title and icon.
- [init(_:image:)](./init%28_,image%29.md)
  Creates a label with an icon image and a title generated from a localized string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:))*