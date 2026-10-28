# init(_:systemImage:role:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a string and a system image and an image resource.

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
nonisolated init<S>(_ title: S, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s `action`.
- `systemImage`: The name of the image resource to lookup.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user interacts with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:role:action:)-32hud)*