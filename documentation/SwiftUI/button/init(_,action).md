# init(_:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a localized string resource.

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
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init<S>(_ title: S, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the button’s localized title, that describes the purpose of the button’s `action`.
- `action`: The action to perform when the user triggers the button.

## See Also

### Creating a button
- [init(action: () -> Void, label: () -> Label)](./init%28action,label%29.md)
  Creates a button that displays a custom label.
- [init(_:image:action:)](./init%28_,image,action%29.md)
  Creates a button that generates its label from a localized string resource and image resource.
- [init(_:systemImage:action:)](./init%28_,systemimage,action%29.md)
  Creates a button that generates its label from a localized string key and system image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:action:))*