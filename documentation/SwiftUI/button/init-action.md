# init(_:action:)

**Framework**: SwiftUI  
**Kind**: init

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

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes   the purpose of the button’s  .
- `action`: The action to perform when the user triggers the button.

## See Also

- [init(action: () -> Void, label: () -> Label)](button/init(action:label:).md)
  Creates a button that displays a custom label.
- [init(_:image:action:)](button/init(_:image:action:).md)
  Creates a button that generates its label from a localized string key and image resource.
- [init(_:systemImage:action:)](button/init(_:systemimage:action:).md)
  Creates a button that generates its label from a localized string key and system image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:action:))*