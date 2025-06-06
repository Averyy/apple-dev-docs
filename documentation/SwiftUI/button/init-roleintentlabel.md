# init(role:intent:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button with a specified role that performs an `AppIntent`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(role: ButtonRole?, intent: some AppIntent, @ViewBuilder label: () -> Label)
```

## Parameters

- `role`: An optional semantic role describing the button. A value of    means that the button doesn’t have an assigned role.
- `intent`: The   to execute.
- `label`: A view that describes the purpose of the button’s  .

## See Also

- [init(_:intent:)](button/init(_:intent:).md)
  Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init<I>(intent: I, label: () -> Label)](button/init(intent:label:).md)
  Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](button/init(_:role:intent:).md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(_:image:role:intent:)](button/init(_:image:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](button/init(_:systemimage:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(role:intent:label:))*