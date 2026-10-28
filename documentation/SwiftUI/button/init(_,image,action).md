# init(_:image:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a localized string resource and image resource.

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
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, image: ImageResource, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init<S>(_ title: S, image: ImageResource, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the button’s localized title, that describes the purpose of the button’s `action`.
- `image`: The image resource to lookup.
- `action`: The action to perform when the user triggers the button.

## See Also

### Creating a button
- [init(action: () -> Void, label: () -> Label)](./init%28action,label%29.md)
  Creates a button that displays a custom label.
- [init(_:action:)](./init%28_,action%29.md)
  Creates a button that generates its label from a localized string resource.
- [init(_:systemImage:action:)](./init%28_,systemimage,action%29.md)
  Creates a button that generates its label from a localized string key and system image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:image:action:))*