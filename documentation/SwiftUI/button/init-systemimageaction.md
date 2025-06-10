# init(_:systemImage:action:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that generates its label from a localized string key and system image name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, action: @escaping @MainActor () -> Void)
```

## Mentions

- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)

#### Discussion

This initializer creates a [`Label`](label.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes   the purpose of the button’s  .
- `systemImage`: The name of the image resource to lookup.
- `action`: The action to perform when the user triggers the button.

## See Also

- [init(action: () -> Void, label: () -> Label)](button/init(action:label:).md)
  Creates a button that displays a custom label.
- [init(_:action:)](button/init(_:action:).md)
  Creates a button that generates its label from a localized string key.
- [init(_:image:action:)](button/init(_:image:action:).md)
  Creates a button that generates its label from a localized string key and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:action:))*