# init(_:role:action:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button with a specified role that generates its label from a localized string key.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes   the purpose of the button’s  .
- `role`: An optional semantic role describing the button. A value of    means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user triggers the button.

## See Also

- [init(role: ButtonRole?, action: () -> Void, label: () -> Label)](button/init(role:action:label:).md)
  Creates a button with a specified role that displays a custom label.
- [init(_:image:role:action:)](button/init(_:image:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key and an image resource.
- [init(_:systemImage:role:action:)](button/init(_:systemimage:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:role:action:))*