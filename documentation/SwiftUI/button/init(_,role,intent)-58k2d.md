# init(_:role:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that performs an `AppIntent` and generates its label from a localized string key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ title: some StringProtocol, role: ButtonRole?, intent: some AppIntent)
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, role: ButtonRole?, intent: some AppIntent)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `intent`.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `intent`: The `AppIntent` to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:role:intent:)-58k2d)*