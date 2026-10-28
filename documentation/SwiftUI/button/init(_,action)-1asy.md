# init(_:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a localized string key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init<S>(_ title: S, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `action`.
- `action`: The action to perform when the user triggers the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:action:)-1asy)*