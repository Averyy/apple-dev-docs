# init(_:systemImage:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a string and system image name.

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
nonisolated init<S>(_ title: S, systemImage: String, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, action: @escaping @MainActor () -> Void)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, action: @escaping @MainActor () -> Void)
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s `action`.
- `systemImage`: The name of the image resource to lookup.
- `action`: The action to perform when the user triggers the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:action:)-23bvz)*