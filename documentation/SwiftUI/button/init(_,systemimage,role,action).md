# init(_:systemImage:role:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a localized string key and a system image.

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
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `action`.
- `systemImage`: The name of the image resource to lookup.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user triggers the button.

## See Also

### Creating a button with a role
- [init(role: ButtonRole?, action: () -> Void, label: () -> Label)](./init%28role,action,label%29.md)
  Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](./init%28_,role,action%29.md)
  Creates a button with a specified role that generates its label from a localized string resource.
- [init(_:image:role:action:)](./init%28_,image,role,action%29.md)
  Creates a button with a specified role that generates its label from a localized string resource and an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:role:action:))*