# init(intent:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that performs an `AppIntent`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init<I>(intent: I, @ViewBuilder label: () -> Label) where I : AppIntent
```

## Parameters

- `intent`: The   to execute.
- `label`: A view that describes the purpose of the button’s  .

## See Also

- [init(_:intent:)](button/init(_:intent:).md)
  Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init(_:role:intent:)](button/init(_:role:intent:).md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](button/init(role:intent:label:).md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](button/init(_:image:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](button/init(_:systemimage:role:intent:).md)
  Creates a button with a specified role that generates its label from a string and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(intent:label:))*