# init(_:role:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a string.

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
@preconcurrency
nonisolated init<S>(_ title: S, role: ButtonRole?, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s `action`.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user interacts with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:role:action:)-8y5yk)*