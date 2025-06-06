# init(_:intent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that performs an `AppIntent` and generates its label from a localized string key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, intent: some AppIntent)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

To initialize a button with a string variable, use [`init(_:intent:)`](button/init(_:intent:).md) instead.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes   the purpose of the button’s  .
- `intent`: The   to execute.

## See Also

- [init<I>(intent: I, label: () -> Label)](button/init(intent:label:).md)
  Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](button/init(_:role:intent:).md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](button/init(role:intent:label:).md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](button/init(_:image:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](button/init(_:systemimage:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:intent:))*