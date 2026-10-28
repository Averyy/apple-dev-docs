# init(_:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that performs an `AppIntent` and generates its label from a localized string key.

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
init(_ titleKey: LocalizedStringKey, intent: some AppIntent)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, intent: some AppIntent)
```

```swift
nonisolated
init<S>(_ title: S, intent: some AppIntent) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

To initialize a button with a string variable, use [`init(_:intent:)`](./init%28_,intent%29.md) instead.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `intent`.
- `intent`: The `AppIntent` to execute.

## See Also

### Creating a button to perform an App Intent
- [init<I>(intent: I, label: () -> Label)](./init%28intent,label%29.md)
  Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](./init%28_,role,intent%29.md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](./init%28role,intent,label%29.md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](./init%28_,image,role,intent%29.md)
  Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](./init%28_,systemimage,role,intent%29.md)
  Creates a button with a specified role that generates its label from a string and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:intent:))*