# init(_:systemImage:role:intent:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button with a specified role that generates its label from a string and a system image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ title: some StringProtocol, systemImage: String, role: ButtonRole? = nil, intent: some AppIntent)
```

#### Discussion

This initializer creates a [`Label`](label.md) view on your behalf, and treats the title similar to [`init(_:)`](text/init(_:)-9d1g4.md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s  .
- `systemImage`: The name of the image resource to lookup.
- `role`: An optional semantic role describing the button. A value of    means that the button doesn’t have an assigned role.
- `intent`: The   to execute.

## See Also

- [init(_:intent:)](button/init(_:intent:).md)
  Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init<I>(intent: I, label: () -> Label)](button/init(intent:label:).md)
  Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](button/init(_:role:intent:).md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](button/init(role:intent:label:).md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](button/init(_:image:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:role:intent:))*