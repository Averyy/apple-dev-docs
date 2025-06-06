# init(_:image:role:action:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button with a specified role that generates its label from a localized string key and an image resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

#### Discussion

This initializer creates a [`Label`](label.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes   the purpose of the button’s  .
- `image`: The image resource to lookup.
- `role`: An optional semantic role describing the button. A value of    means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user triggers the button.

## See Also

- [init(role: ButtonRole?, action: () -> Void, label: () -> Label)](button/init(role:action:label:).md)
  Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](button/init(_:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key.
- [init(_:systemImage:role:action:)](button/init(_:systemimage:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:image:role:action:))*