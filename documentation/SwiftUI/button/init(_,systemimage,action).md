# init(_:systemImage:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, action: @escaping @MainActor () -> Void)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Mentions

- [Populating SwiftUI menus with adaptive controls](../populating-swiftui-menus-with-adaptive-controls.md)

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `action`.
- `systemImage`: The name of the image resource to lookup.
- `action`: The action to perform when the user triggers the button.

## See Also

### Creating a button
- [init(action: () -> Void, label: () -> Label)](./init%28action,label%29.md)
  Creates a button that displays a custom label.
- [init(_:action:)](./init%28_,action%29.md)
  Creates a button that generates its label from a localized string resource.
- [init(_:image:action:)](./init%28_,image,action%29.md)
  Creates a button that generates its label from a localized string resource and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:action:))*