# init(_:role:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init<S>(_ title: S, role: ButtonRole?, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the button’s localized title, that describes the purpose of the button’s `action`.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user triggers the button.

## See Also

### Creating a button with a role
- [init(role: ButtonRole?, action: () -> Void, label: () -> Label)](./init%28role,action,label%29.md)
  Creates a button with a specified role that displays a custom label.
- [init(_:image:role:action:)](./init%28_,image,role,action%29.md)
  Creates a button with a specified role that generates its label from a localized string resource and an image resource.
- [init(_:systemImage:role:action:)](./init%28_,systemimage,role,action%29.md)
  Creates a button with a specified role that generates its label from a localized string key and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:role:action:))*