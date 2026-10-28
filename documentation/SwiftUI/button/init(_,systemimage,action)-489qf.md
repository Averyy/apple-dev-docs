# init(_:systemImage:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a localized string resource and system image name.

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, action: @escaping @MainActor () -> Void)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the button’s localized title, that describes the purpose of the button’s `action`.
- `systemImage`: The name of the image resource to lookup.
- `action`: The action to perform when the user triggers the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:action:)-489qf)*