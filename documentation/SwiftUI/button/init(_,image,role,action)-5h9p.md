# init(_:image:role:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a string and an image resource.

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
nonisolated init<S>(_ title: S, image: ImageResource, role: ButtonRole?, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s `action`.
- `image`: The image resource to lookup.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user interacts with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:image:role:action:)-5h9p)*